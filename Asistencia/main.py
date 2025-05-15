import sys
from antlr4 import *
from AsistenciaLexer import AsistenciaLexer
from AsistenciaParser import AsistenciaParser
from AsistenciaVisitor import AsistenciaVisitor
import pandas as pd
import os
from pathlib import Path
import tempfile

class AsistenciaInterpreter(AsistenciaVisitor):
    def __init__(self):
        self.data = None
        self.filters = []
        self.aggregates = []

    def visitProgram(self, ctx):
        for instr in ctx.instruction():
            self.visit(instr)

    def visitLoadStmt(self, ctx):
        filename = ctx.STRING().getText().strip('"')
        base_dir = Path(__file__).parent
        csv_path = base_dir / filename
        
        try:
            self.data = pd.read_csv(csv_path)
            print(f"[INFO] Archivo CSV cargado: {csv_path}")
        except FileNotFoundError:
            print(f"[ERROR] No se encontró el archivo: {csv_path}")
            print(f"[INFO] Directorio actual: {base_dir}")
            print(f"[INFO] Archivos disponibles: {os.listdir(base_dir)}")

    def visitFilterStmt(self, ctx):
        expr = ""
        for child in ctx.filterExpr().children:
            text = child.getText()
            if text == "column":
                continue
            elif text in ["AND", "OR"]:
                expr += f" {text.lower()} "
            elif hasattr(child, "STRING"):
                col = child.STRING().getText().strip('"')
                op = child.OPERATOR().getText()
                val_token = child.value().getText()
                try:
                    val = float(val_token)
                except ValueError:
                    if val_token.startswith('"') and val_token.endswith('"'):
                        val_token = val_token[1:-1]
                    val = f'"{val_token}"'
                expr += f"(`{col}` {op} {val})"
        if expr:
            self.filters.append(expr)

    def visitAggregateStmt(self, ctx):
        op = ctx.AGG_OP().getText().lower()
        col = ctx.STRING().getText().strip('"')
        self.aggregates.append((op, col))

    def visitPrintStmt(self, ctx):
        if self.data is None:
            print("[ERROR] No se ha cargado un archivo CSV.")
            return

        df = self.data.copy()
        if self.filters:
            combined_filter = " & ".join(self.filters)
            try:
                df = df.query(combined_filter)
                print(f"[INFO] Filtro aplicado: {combined_filter}")
            except Exception as e:
                print(f"[ERROR] Filtro inválido: {combined_filter}")
                print(e)
                return

        for op, col in self.aggregates:
            try:
                if op == 'count':
                    result = df[col].count()
                elif op == 'sum':
                    result = df[col].sum()
                elif op == 'average':
                    result = df[col].mean()
                print(f"{op.upper()}({col}): {result}")
            except Exception as e:
                print(f"[ERROR] No se pudo procesar {op.upper()}({col})")
                print(e)

        self.filters = []
        self.aggregates = []

def ejecutar_script(path):
    print(f"\n[INFO] Ejecutando script: {path}")
    input_stream = FileStream(path, encoding='utf-8')
    lexer = AsistenciaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = AsistenciaParser(stream)
    tree = parser.program()
    visitor = AsistenciaInterpreter()
    visitor.visit(tree)
    input("\nPresione Enter para continuar...")

def extraer_scripts(script_path):
    """Extrae los 40 scripts individuales del archivo consolidado"""
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    script_blocks = []
    current_script = []
    
    for line in content.split('\n'):
        if line.startswith('# Script'):
            if current_script:
                script_blocks.append('\n'.join(current_script))
                current_script = []
        current_script.append(line)
    
    if current_script:
        script_blocks.append('\n'.join(current_script))
    
    return script_blocks

def mostrar_menu_scripts(scripts):
    """Muestra un menú con los 40 scripts disponibles"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "="*60)
        print(" SELECCIÓN DE SCRIPTS - ELIJA UNO DE LOS 40 DISPONIBLES ".center(60))
        print("="*60)
        
        for i in range(0, 40, 10):
            for j in range(1, 11):
                idx = i + j
                if idx <= len(scripts):
                    print(f"{idx:2d}. Script {idx}")
            print("-"*60)
            if i < 30:
                input("Presione Enter para ver más scripts...")
                os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n0. Volver al menú principal")
        print("="*60)
        
        try:
            opcion = input("\nSeleccione un script (1-40) o 0 para volver: ")
            if opcion == "0":
                return
            opcion = int(opcion)
            if 1 <= opcion <= 40:
                with tempfile.NamedTemporaryFile(mode='w+', suffix='.dsl', delete=False) as temp:
                    temp.write(scripts[opcion-1])
                    temp_path = temp.name
                
                ejecutar_script(temp_path)
                os.unlink(temp_path)
            else:
                print("\n[ERROR] El número debe estar entre 1 y 40")
                input("Presione Enter para continuar...")
        except ValueError:
            print("\n[ERROR] Ingrese un número válido")
            input("Presione Enter para continuar...")

def mostrar_menu_principal():
    base_dir = Path(__file__).parent
    script_path = base_dir / "script.dsl"
    csv_path = base_dir / "asistencia_completa.csv"
    
    if not script_path.exists():
        print(f"[ERROR] No se encontró script.dsl en {base_dir}")
        return
    
    scripts = extraer_scripts(script_path)
    if not scripts:
        print("[ERROR] No se pudieron extraer scripts del archivo")
        return
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "="*50)
        print(" SISTEMA DE ANÁLISIS DE ASISTENCIA ".center(50))
        print("="*50)
        print("\n1. Seleccionar script (1-40)")
        print("2. Ver archivo CSV completo")
        print("3. Ver lista completa de scripts")
        print("0. Salir")
        print("="*50)
        
        try:
            opcion = input("\nSeleccione una opción: ")
            if opcion == "0":
                break
            elif opcion == "1":
                mostrar_menu_scripts(scripts)
            elif opcion == "2":
                if csv_path.exists():
                    df = pd.read_csv(csv_path)
                    print(f"\nPrimeras 10 filas del CSV:\n{df.head(10)}")
                else:
                    print(f"\n[ERROR] No se encontró {csv_path}")
                input("\nPresione Enter para continuar...")
            elif opcion == "3":
                print("\nLISTA COMPLETA DE SCRIPTS DISPONIBLES:")
                for i, script in enumerate(scripts, 1):
                    first_line = script.split('\n')[0]
                    print(f"{i:2d}. {first_line}")
                input("\nPresione Enter para continuar...")
            else:
                print("\nOpción no válida")
                input("Presione Enter para continuar...")
        except Exception as e:
            print(f"\n[ERROR] {e}")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ejecutar_script(sys.argv[1])
    else:
        mostrar_menu_principal()
import sys
from antlr4 import *
from AsistenciaLexer import AsistenciaLexer
from AsistenciaParser import AsistenciaParser
from AsistenciaVisitor import AsistenciaVisitor
import pandas as pd
import os
from pathlib import Path
import tempfile
from antlr4.tree.Trees import Trees
import graphviz
from AsistenciaInterpreter import AsistenciaInterpreter

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

def generar_arbol_sintactico(tree, parser, output_file="arbol_sintactico"):
    # Cambia la ruta de salida para guardar en la carpeta 'arboles'
    base_dir = Path(__file__).parent
    arboles_dir = base_dir / "arboles"
    arboles_dir.mkdir(exist_ok=True)
    output_path = arboles_dir / output_file

    dot = graphviz.Digraph()

    def agregar_nodos(node, parent=None):
        node_id = str(id(node))
        if hasattr(node, 'getRuleIndex'):
            rule_index = node.getRuleIndex()
            label = parser.ruleNames[rule_index] if rule_index < len(parser.ruleNames) else f"rule_{rule_index}"
        else:
            label = node.getText()
        dot.node(node_id, label)
        if parent:
            dot.edge(parent, node_id)
        for i in range(node.getChildCount()):
            agregar_nodos(node.getChild(i), node_id)

    agregar_nodos(tree)
    dot.render(str(output_path), format='png', cleanup=True)
    print(f"[INFO] Árbol visual guardado como: {output_path}.png")

def ejecutar_script(path, mostrar_arbol=False, numero_script=None):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Filtrar líneas de comentario
        content = '\n'.join(line for line in content.split('\n') 
                  if not line.strip().startswith('#'))
        
        input_stream = InputStream(content)
        lexer = AsistenciaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = AsistenciaParser(stream)
        tree = parser.program()
        AsistenciaInterpreter().visit(tree)
        
        if mostrar_arbol:
            generar_arbol_sintactico(tree, parser, f"arbol_script_{numero_script}")
            
    except Exception as e:
        print(f"\n[ERROR] En script {numero_script}: {str(e)}")
    finally:
        input("\nPresione Enter para continuar...")

def extraer_scripts(script_path):
    encodings = ['utf-8-sig', 'utf-8', 'latin-1']
    for encoding in encodings:
        try:
            with open(script_path, 'r', encoding=encoding) as f:
                content = f.read()
                break
        except UnicodeDecodeError:
            continue
    else:
        raise ValueError("No se pudo leer el archivo con los encodings probados")

    script_blocks = []
    current_script = []
    
    for line in content.split('\n'):
        stripped = line.strip()
        if stripped.startswith('# Script'):
            if current_script:
                script_blocks.append('\n'.join(current_script))
                current_script = []
        if not stripped.startswith('#'):  # Ignorar líneas de comentario
            current_script.append(line)
    
    if current_script:
        script_blocks.append('\n'.join(current_script))
    
    return script_blocks

def mostrar_menu_scripts(scripts):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "="*60)
        print(" SELECCIÓN DE SCRIPTS ".center(60))
        print(f" Disponibles: {len(scripts)} scripts ".center(60))
        print("="*60)
        
        for i, script in enumerate(scripts, 1):
            # Extraer primera línea no comentada como descripción
            description = next((line.strip() for line in script.split('\n') 
                             if line.strip() and not line.strip().startswith('#')), 
                            f"Script {i}")
            print(f"{i:2d}. {description[:50]}")  # Mostrar primeros 50 caracteres

        print("\n0. Volver al menú principal")
        print("="*60)

        try:
            opcion = input("\nSeleccione un script (1-{}) o 0 para volver: ".format(len(scripts))).strip()
            
            if not opcion or not opcion.isdigit():
                raise ValueError("Debe ingresar un número válido")
                
            opcion = int(opcion)
            
            if opcion == 0:
                return
            elif 1 <= opcion <= len(scripts):
                # Preprocesar script: eliminar líneas que comienzan con #
                clean_script = '\n'.join(line for line in scripts[opcion-1].split('\n') 
                              if not line.strip().startswith('#'))
                
                with tempfile.NamedTemporaryFile(mode='w+', suffix='.dsl', 
                                              encoding='utf-8', delete=False) as temp:
                    temp.write(clean_script)
                    temp_path = temp.name
                
                ejecutar_script(temp_path, mostrar_arbol=True, numero_script=opcion)
                os.unlink(temp_path)
            else:
                raise ValueError(f"Número fuera de rango (1-{len(scripts)})")
                
        except Exception as e:
            print(f"\n[ERROR] {str(e)}")
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
        print("\n" + "=" * 50)
        print(" SISTEMA DE ANÁLISIS DE ASISTENCIA ".center(50))
        print("=" * 50)
        print("\n1. Seleccionar script (1-40)")
        print("2. Ver archivo CSV completo")
        print("3. Ver lista completa de scripts")
        print("0. Salir")
        print("=" * 50)

        try:
            opcion = input("\nSeleccione una opción: ").strip()

            if not opcion.isdigit():
                raise ValueError("Debe ingresar un número (0-3).")

            opcion = int(opcion)

            if opcion == 0:
                break
            elif opcion == 1:
                mostrar_menu_scripts(scripts)
            elif opcion == 2:
                if csv_path.exists():
                    df = pd.read_csv(csv_path)
                    print(f"\nPrimeras 10 filas del CSV:\n{df.head(10)}")
                else:
                    print(f"\n[ERROR] No se encontró el archivo CSV en: {csv_path}")
                input("\nPresione Enter para continuar...")
            elif opcion == 3:
                print("\nLISTA COMPLETA DE SCRIPTS DISPONIBLES:")
                for i, script in enumerate(scripts, 1):
                    first_line = script.split('\n')[0]
                    print(f"{i:2d}. {first_line}")
                input("\nPresione Enter para continuar...")
            else:
                print("\n[ERROR] Opción fuera de rango. Debe ser entre 0 y 3.")
                input("Presione Enter para continuar...")

        except ValueError as ve:
            print(f"\n[ERROR] {ve}")
            input("Presione Enter para continuar...")
        except Exception as e:
            print(f"\n[ERROR inesperado] {e}")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            ejecutar_script(sys.argv[1], mostrar_arbol=True)
        else:
            mostrar_menu_principal()
    except Exception as e:
        print(f"\n[ERROR fatal] {e}")
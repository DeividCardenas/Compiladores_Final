import sys
from antlr4 import *
from AsistenciaLexer import AsistenciaLexer
from AsistenciaParser import AsistenciaParser
from AsistenciaVisitor import AsistenciaVisitor
import pandas as pd

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
        self.data = pd.read_csv(filename)
        print(f"[INFO] Archivo CSV '{filename}' cargado.")

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
                    # Usar un enfoque más simple para evitar problemas de escape
                    if val_token.startswith('"') and val_token.endswith('"'):
                        val_token = val_token[1:-1]  # Quitar comillas externas
                    val = f'"{val_token}"'
                # No incluir 'df[]' en la expresión de filtro para pandas.query()
                expr += f"(`{col}` {op} {val})"
        if expr:
            self.filters.append(expr)
        else:
            print("[ADVERTENCIA] No se construyó ningún filtro válido.")

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
            combined_filter = self.filters[0]
            for f in self.filters[1:]:
                combined_filter += f
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
                else:
                    result = '[ERROR] Operación no válida'
                print(f"{op.upper()}({col}): {result}")
            except Exception as e:
                print(f"[ERROR] No se pudo procesar la agregación {op.upper()}({col})")
                print(e)

        # Limpiar después de imprimir
        self.filters = []
        self.aggregates = []

def ejecutar_script(path):
    print(f"[INFO] Ejecutando script: {path}")
    input_stream = FileStream(path, encoding='utf-8')
    lexer = AsistenciaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = AsistenciaParser(stream)
    tree = parser.program()
    print("[INFO] Análisis sintáctico completado")
    visitor = AsistenciaInterpreter()
    visitor.visit(tree)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py script.dsl")
    else:
        ejecutar_script(sys.argv[1])
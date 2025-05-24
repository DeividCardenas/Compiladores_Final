from AsistenciaVisitor import AsistenciaVisitor
import pandas as pd

class AsistenciaInterpreter(AsistenciaVisitor):
    def __init__(self):
        self.data = None  # DataFrame para almacenar datos del CSV
        self.filters = []  # Lista de condiciones de filtrado
        self.aggregates = []  # Lista de operaciones de agregación

    def visitLoadStmt(self, ctx):
        # Lógica para cargar archivos CSV
        filename = ctx.STRING().getText().strip('"')
        try:
            self.data = pd.read_csv(filename)
            print(f"[INFO] CSV cargado: {filename}")
        except FileNotFoundError:
            print(f"[ERROR] Archivo no encontrado: {filename}")

    def visitFilterStmt(self, ctx):
        # Lógica para filtros (ej: "filter column 'notas' >= 3.5")
        columna = ctx.STRING().getText().strip('"')
        operador = ctx.OPERATOR().getText()
        valor = ctx.value().getText()
        self.filters.append(f"{columna} {operador} {valor}")

    def visitAggregateStmt(self, ctx):
        # Lógica para agregaciones (ej: "aggregate count column 'id'")
        operacion = ctx.AGG_OP().getText()  # 'count', 'sum', etc.
        columna = ctx.STRING().getText().strip('"')
        self.aggregates.append((operacion, columna))

    def visitPrintStmt(self, ctx):
        # Lógica para imprimir resultados
        if self.data is None:
            print("[ERROR] No hay datos cargados")
            return

        # Aplicar filtros
        if self.filters:
            query = " & ".join(self.filters)
            self.data = self.data.query(query)

        # Aplicar agregaciones
        for op, col in self.aggregates:
            if op == "count":
                print(f"Total: {self.data[col].count()}")
            elif op == "sum":
                print(f"Suma: {self.data[col].sum()}")

        self.filters = []
        self.aggregates = []

    def visitScriptComment(self, ctx):
        # Ignorar comentarios (ej: "# Script 1: ...")
        pass
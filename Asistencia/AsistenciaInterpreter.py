import os
import pandas as pd
from AsistenciaVisitor import AsistenciaVisitor

class AsistenciaInterpreter(AsistenciaVisitor):
    def __init__(self):
        self.data = None
        self.filters = []
        self.aggregates = []

    def visitLoad(self, ctx):
        import os
        filename = ctx.STRING().getText().strip('"')
        print(f"[Debug] Directorio de trabajo actual: {os.getcwd()}")
        print(f"[Debug] Intentando cargar archivo CSV: {filename}")
        try:
            with open(filename, newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                self.data = list(reader)
                print(f"[Debug] Columnas detectadas: {reader.fieldnames}")
                if len(self.data) == 0:
                    print("[Error] El archivo se abrió, pero está vacío.")
                else:
                    print(f"[Debug] Archivo cargado correctamente. Filas: {len(self.data)}")
                    print(f"[Debug] Primera fila: {self.data[0]}")
        except FileNotFoundError:
            print(f"[Error] Archivo no encontrado: {filename}")
            self.data = None
        except Exception as e:
            print(f"[Error] Error al cargar CSV: {e}")
            self.data = None

    def visitFilterStmt(self, ctx):
        if self.data is None:
            print("[ERROR] No se han cargado datos. Usa 'load \"archivo.csv\"' primero.")
            return

        columna = ctx.STRING().getText().strip('"')
        operador = ctx.OPERATOR().getText()
        valor_raw = ctx.value().getText()

        if columna not in self.data.columns:
            print(f"[ERROR] La columna '{columna}' no existe en los datos.")
            return

        # Convertir valor a tipo apropiado
        try:
            valor = eval(valor_raw)
        except Exception:
            valor = f'"{valor_raw.strip()}"' 

        expresion = f"`{columna}` {operador} {valor}"
        self.filters.append(expresion)
        print(f"[INFO] Filtro agregado: {expresion}")

    def visitAggregateStmt(self, ctx):
        if self.data is None:
            print("[ERROR] No hay datos cargados. Usa 'load' primero.")
            return

        operacion = ctx.AGG_OP().getText().lower()
        columna = ctx.STRING().getText().strip('"')

        if columna not in self.data.columns:
            print(f"[ERROR] La columna '{columna}' no existe.")
            return

        if operacion not in ["count", "sum", "mean", "max", "min"]:
            print(f"[ERROR] Operación de agregación '{operacion}' no soportada.")
            return

        self.aggregates.append((operacion, columna))
        print(f"[INFO] Agregación registrada: {operacion}({columna})")

    def visitPrintStmt(self, ctx):
        if self.data is None:
            print("[ERROR] No hay datos cargados. ¿Olvidaste el 'load'?")
            return

        print("[Debug] Datos cargados. Aplicando filtros y agregaciones...")

        df_filtrado = self.data

        if self.filters:
            try:
                query_str = " & ".join(self.filters)
                df_filtrado = df_filtrado.query(query_str)
                print(f"[INFO] Filtros aplicados: {query_str}")
            except Exception as e:
                print(f"[ERROR] Fallo al aplicar filtros: {e}")
                return

        if self.aggregates:
            self._apply_aggregates(df_filtrado)
        else:
            print("[INFO] Mostrando las primeras 5 filas del resultado:")
            print(df_filtrado.head())

        # Limpiar después de imprimir
        self.filters = []
        self.aggregates = []

    def _apply_aggregates(self, df_filtrado):
        for op, col in self.aggregates:
            try:
                resultado = None
                if op == "count":
                    resultado = df_filtrado[col].count()
                elif op == "sum":
                    resultado = df_filtrado[col].sum()
                elif op == "mean":
                    resultado = df_filtrado[col].mean()
                elif op == "max":
                    resultado = df_filtrado[col].max()
                elif op == "min":
                    resultado = df_filtrado[col].min()

                print(f"{op.upper()}({col}): {resultado}")

            except Exception as e:
                print(f"[ERROR] Fallo al aplicar agregación '{op}' en columna '{col}': {e}")

    def visitScriptComment(self, ctx):
        # Comentarios ignorados
        pass

# Compiladores_Final

Este repositorio contiene el proyecto final para la clase de Compiladores, que consiste en el diseño e implementación de un intérprete para un lenguaje específico de dominio (DSL) orientado a la consulta y análisis de datos de asistencia escolar en archivos CSV.

El lenguaje permite ejecutar operaciones como cargar archivos, aplicar filtros condicionales combinados con operadores lógicos (AND, OR), realizar agregaciones (count, sum, average) y mostrar los resultados, todo a través de una sintaxis sencilla y personalizada, diseñada con ANTLR4.

## Descripción

Este proyecto implementa un intérprete completo que incluye:

- Análisis léxico
- Análisis sintáctico
- Análisis semántico 
- Interpretación/Ejecución

El intérprete está desarrollado en Python y permite la ejecución de programas escritos en un lenguaje similar a Pascal con características propias.

## Estructura del Proyecto

```
Asistencia/
├── __pycache__/                  # Archivos compilados por Python
├── arboles/                      # Visualizaciones de árboles generados
│   └── arbol_script_02...       
├── arbol_sintactico...           # Árbol sintáctico generado (fuera de /arboles)
├── asistencia_comp...            # Archivo de prueba o comparación (fuera de /arboles)
├── Asistencia.g4                 # Gramática ANTLR para el DSL
├── Asistencia.interp             # Archivo auxiliar ANTLR
├── Asistencia.tokens             # Tokens generados por ANTLR
├── AsistenciaLexer.interp       # Archivo auxiliar ANTLR (Lexer)
├── AsistenciaLexer.py           # Lexer generado por ANTLR
├── AsistenciaLexer.tokens       # Tokens del Lexer
├── AsistenciaListener.py        # Listener generado por ANTLR
├── AsistenciaParser.py          # Parser generado por ANTLR
├── AsistenciaVisitor.py         # Visitor generado por ANTLR
├── generar_datos.py             # Script para generar datos CSV de ejemplo
├── main.py                      # Script principal que interpreta el DSL
└── script.dsl                   # Archivo de entrada con comandos en el DSL

```

## Características del Lenguaje

El lenguaje soporta:

- Declaración de variables con tipado estático
- Estructuras de control: if-else, while, for
- Funciones y procedimientos
- Manejo de ámbitos y tablas de símbolos
- Tipos de datos: enteros, reales, booleanos, strings y arreglos
- Expresiones aritméticas, relacionales y lógicas
- Entrada/salida básica

## Tecnologías y Librerías Utilizadas

- Python 3.6 o superior
- ANTLR4 – Generador de analizadores léxicos y sintácticos
- pandas – Manipulación de datos tabulares (CSV)
- os – Interacción con el sistema de archivos
- pathlib – Manejo de rutas de archivos de forma orientada a objetos
- tempfile – Creación de archivos y directorios temporales
- graphviz – Visualización de árboles sintácticos




## Gramática del Lenguaje

El archivo Asistencia.g4 define la gramática del lenguaje específico de dominio (DSL) para consultar archivos CSV de asistencia escolar. Esta gramática fue desarrollada usando ANTLR4 y permite interpretar comandos simples como cargar datos, filtrarlos, aplicar agregaciones y mostrar resultados.

```
grammar Asistencia;

program: instruction+;

instruction
    : loadStmt
    | filterStmt
    | aggregateStmt
    | printStmt
    ;

loadStmt: 'load' STRING ';';
filterStmt: 'filter' filterExpr ';';
filterExpr: condition (LOGICAL_OP condition)*;
condition: 'column' STRING OPERATOR value;
aggregateStmt: 'aggregate' AGG_OP 'column' STRING ';';
printStmt: 'print' ';';

value: STRING | NUMBER;

STRING: '"' (~["\r\n])* '"';
NUMBER: [0-9]+ ('.' [0-9]+)?;
OPERATOR: '>=' | '<=' | '>' | '<' | '==' | '!=';
LOGICAL_OP: 'AND' | 'OR';
AGG_OP: 'count' | 'sum' | 'average';

WS: [ \t\r\n]+ -> skip;

```

## Instalación y Ejecucion

1. Requisitos previos
- verificamos nuestra version de java con: 
```
java -version
```
- Instalamos Antlr4 y dependencias con los comandos:

```
pip install antlr4-tools
pip install antlr4-python3-runtime
```

2. Creamos nuestro archivo .g4 en este caso Asistencia.g4
dentro de Asistencia.g4 pegamos nuestro codigo de consulta

3. Generar Lexer, Parser y Visitor: 
```
antlr4 -Dlanguage=Python3 -visitor Asistencia.g4
```
4. Crear los archivos del proyecto
Aseguramos de tener los siguientes archivos creados o disponibles:

- main.py – Ejecuta el intérprete del DSL

- interpreter.py – Lógica del intérprete que recorre el árbol sintáctico

- script.dsl – Archivo con las instrucciones escritas en el DSL

- generar_datos.py – Script para generar un archivo CSV de prueba

5. Instalamos librerías adicionales: 
```
pip install pandas graphviz faker

```
6. Generamos archivo CSV de prueba: 
```
python generar_datos.py
```
7. Ejecutamos el programa principal: 
```
python main.py
```

## Autores

Santiago Reyes Sanchez
Deivid Julian Cardenas Melo


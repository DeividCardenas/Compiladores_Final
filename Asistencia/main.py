import sys
import os
from antlr4 import *
from AsistenciaLexer import AsistenciaLexer
from AsistenciaParser import AsistenciaParser
from AsistenciaVisitor import AsistenciaVisitor
import pandas as pd
from pathlib import Path
import tempfile
from antlr4.tree.Trees import Trees
import graphviz
from AsistenciaInterpreter import AsistenciaInterpreter

def mostrar_analisis_lexico(path):
    print("\n1 Análisis Léxico (Tokens generados):")
    input_stream = FileStream(path, encoding='utf-8')
    lexer = AsistenciaLexer(input_stream)
    tokens = []
    token = lexer.nextToken()
    while token.type != Token.EOF:
        tokens.append(f"[{lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) and lexer.symbolicNames[token.type] else token.text}]")
        token = lexer.nextToken()
    print(" ".join(tokens))
    print("")

def generar_arbol_graphviz_png(tree, parser, output_png):
    def escape(s):
        return s.replace('"', '\\"')
    def to_dot(node, ruleNames, node_id=0, nodes=None, edges=None):
        if nodes is None: nodes = []
        if edges is None: edges = []
        label = escape(Trees.getNodeText(node, ruleNames))
        nodes.append(f'  node{node_id} [label="{label}"];')
        this_id = node_id
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            child_id = len(nodes)
            edges.append(f'  node{this_id} -> node{child_id};')
            to_dot(child, ruleNames, child_id, nodes, edges)
        return nodes, edges
    nodes, edges = to_dot(tree, parser.ruleNames)
    dot = "digraph G {\n" + "\n".join(nodes) + "\n" + "\n".join(edges) + "\n}"
    import tempfile
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".gv") as tmpfile:
        tmpfile.write(dot)
        tmpfile_path = tmpfile.name
    try:
        import subprocess
        subprocess.run(["dot", "-Tpng", tmpfile_path, "-o", output_png], check=True)
        print(f"Árbol de sintaxis generado: {output_png}")
    except Exception as e:
        print(f"No se pudo generar el PNG del árbol: {e}")
    finally:
        try:
            os.remove(tmpfile_path)
        except Exception:
            pass

def mostrar_analisis_sintactico(path, parser, tree):
    print("2 Análisis Sintáctico (Árbol de sintaxis):")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    arboles_dir = os.path.join(base_dir, "arboles")
    os.makedirs(arboles_dir, exist_ok=True)
    # Usa el nombre del script seleccionado (sin extensión .dsl)
    nombre = os.path.splitext(os.path.basename(path))[0]
    # Buscar el nombre real del script si existe en script_names
    global script_names
    script_name = None
    for idx, temp_path in script_tempfiles.items():
        if temp_path == path:
            script_name = script_names[idx-1]
            break
    if script_name:
        # Limpia el nombre para archivo (sin espacios ni caracteres especiales)
        from re import sub
        nombre_archivo = sub(r'[^a-zA-Z0-9_]', '_', script_name)
    else:
        nombre_archivo = nombre
    output_png = os.path.join(arboles_dir, f"arbol_{nombre_archivo}.png")
    generar_arbol_graphviz_png(tree, parser, output_png)
    print("")

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
    script_names = []
    current_script = []
    current_name = None
    for line in content.split('\n'):
        stripped = line.strip()
        if stripped.startswith('# Script'):
            if current_script:
                script_blocks.append('\n'.join(current_script))
                script_names.append(current_name if current_name else f"Script {len(script_blocks)}")
                current_script = []
            # Extraer el nombre del script si está presente después de ":"
            if ':' in stripped:
                current_name = stripped.split(':', 1)[1].strip()
            else:
                current_name = stripped
        if not stripped.startswith('#'):  # Ignorar líneas de comentario
            current_script.append(line)
    if current_script:
        script_blocks.append('\n'.join(current_script))
        script_names.append(current_name if current_name else f"Script {len(script_blocks)}")
    return script_blocks, script_names

def ejecutar_script(path, script_display_name=None):
    # Usa el nombre del script para mostrar en encabezado y pie
    nombre_script = script_display_name if script_display_name else os.path.basename(path)
    print(f"\n{'='*60}")
    print(f"        Ejecutando: {nombre_script}".center(60))
    print(f"{'='*60}")
    mostrar_analisis_lexico(path)
    input_stream = FileStream(path, encoding='utf-8')
    lexer = AsistenciaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = AsistenciaParser(stream)
    tree = parser.program()
    mostrar_analisis_sintactico(path, parser, tree)
    
    print(f"{'='*60}")
    print(f"             Fin de: {nombre_script}".center(60))
    print(f"{'='*60}\n")
    input("Presione Enter para volver a la selección de scripts...")

def mostrar_menu(scripts, script_names):
    while True:
        print("\n" + "="*60)
        print(" SISTEMA DE ANÁLISIS DE ASISTENCIA ".center(60))
        print("="*60)
        print("1. Ejecutar un script")
        print("2. Ver todos los scripts (sin ejecutar)")
        print("0. Salir")
        print("="*60)

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.\n")
            continue

        if opcion == 0:
            print("Saliendo del programa.")
            for temp_path in script_tempfiles.values():
                if os.path.exists(temp_path):
                    os.unlink(temp_path)
            break
        elif opcion == 1:
            while True:
                print("\n" + "="*60)
                print(" SELECCIÓN DE SCRIPTS ".center(60))
                print("="*60)
                print("Seleccione un script para ejecutar:\n")
                for idx, name in enumerate(script_names, 1):
                    print(f" {idx:2d}. {name}")
                print("\n  0. Volver al menú principal")
                print("="*60)
                try:
                    subop = int(input("Ingrese el número del script a ejecutar (0 para volver): "))
                except ValueError:
                    print("Por favor, ingrese un número válido.\n")
                    continue
                if subop == 0:
                    break
                elif 1 <= subop <= len(scripts):
                    if subop not in script_tempfiles:
                        with tempfile.NamedTemporaryFile(mode='w+', suffix='.dsl', encoding='utf-8', delete=False) as temp:
                            temp.write(scripts[subop - 1])
                            temp_path = temp.name
                        script_tempfiles[subop] = temp_path
                    else:
                        temp_path = script_tempfiles[subop]
                    try:
                        ejecutar_script(temp_path, script_display_name=script_names[subop-1])
                    except Exception as e:
                        print(f"[ERROR] {e}")
                else:
                    print("Opción no válida. Intente de nuevo.\n")
        elif opcion == 2:
            print("\n" + "="*60)
            print(" LISTA DE SCRIPTS DISPONIBLES ".center(60))
            print("="*60)
            for idx, name in enumerate(script_names, 1):
                print(f"\n{'-'*60}\nScript {idx}: {name}\n{'-'*60}")
                print(scripts[idx-1])
            print("\nPresione Enter para volver al menú principal.")
            input()
        else:
            print("Opción no válida. Intente de nuevo.\n")

if __name__ == "__main__":
    script_path = "script.dsl"
    base_dir = Path(__file__).parent
    script_path_full = str(base_dir / script_path)
    scripts, script_names = extraer_scripts(script_path_full)
    script_tempfiles = {}
    mostrar_menu(scripts, script_names)
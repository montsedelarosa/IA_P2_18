# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install ply

import ply.yacc as yacc

# Definición de tokens (previamente definidos en el análisis léxico)
tokens = [
    'NUMBER',
    'PLUS',
    'TIMES',
    'LPAREN',
    'RPAREN',
]

# Reglas de gramática ambigua
def p_expression(p):
    """
    expression : expression PLUS expression
               | expression TIMES expression
               | LPAREN expression RPAREN
               | NUMBER
    """
    p[0] = ('expression', p[1:])  # Almacena el árbol de análisis

# Manejo de errores sintácticos
def p_error(p):
    print(f"Error sintáctico en línea {p.lineno}: Token inesperado '{p.value}'")

# Crear el analizador sintáctico
parser = yacc.yacc()

# Función para analizar expresiones y mostrar árboles de análisis
def analyze_expression(expression):
    parsed = parser.parse(expression)
    print(f"Análisis de la expresión: {expression}")
    print(parsed)

# Ejemplos de expresiones ambiguas
expression1 = "2 + 3 * 4"
expression2 = "(2 + 3) * 4"

analyze_expression(expression1)
analyze_expression(expression2)

# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install ply

import ply.yacc as yacc

# Definición de tokens (previamente definidos en el análisis léxico)
tokens = [
    'IF', 'ELSE', 'WHILE', 'FOR',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMICOLON',
    'INT', 'FLOAT', 'NUMBER', 'IDENTIFIER',
]

# Reglas de gramática para estructuras de control de flujo
def p_statement_if(p):
    "statement : IF LPAREN condition RPAREN LBRACE statements RBRACE"
    p[0] = ("IF", p[3], p[6])

def p_statement_if_else(p):
    "statement : IF LPAREN condition RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE"
    p[0] = ("IF_ELSE", p[3], p[6], p[10])

def p_condition(p):
    "condition : expression"
    p[0] = p[1]

def p_expression(p):
    "expression : IDENTIFIER"
    p[0] = ("VARIABLE", p[1])

def p_expression_number(p):
    "expression : NUMBER"
    p[0] = ("NUMBER", p[1])

def p_statements(p):
    "statements : statement SEMICOLON statements"
    p[0] = [p[1]] + p[3]

def p_statements_empty(p):
    "statements :"
    p[0] = []

# Manejo de errores sintácticos
def p_error(p):
    print(f"Error sintáctico en línea {p.lineno}: Token inesperado '{p.value}'")

# Crear el analizador sintáctico
parser = yacc.yacc()

# Código fuente de ejemplo
source_code = """
if (x > 0) {
    y = y * 2;
} else {
    y = y / 2;
}
"""

# Analizar el código fuente
parsed_code = parser.parse(source_code)

# Imprimir la estructura sintáctica resultante
print(parsed_code)

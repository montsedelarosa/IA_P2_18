# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

import re

# Definición de expresiones regulares para tokens comunes
tokens = [
    (r'if', 'IF'),
    (r'else', 'ELSE'),
    (r'while', 'WHILE'),
    (r'for', 'FOR'),
    (r'int', 'INT'),
    (r'float', 'FLOAT'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r'\{', 'LBRACE'),
    (r'\}', 'RBRACE'),
    (r';', 'SEMICOLON'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'\*', 'MULTIPLY'),
    (r'\/', 'DIVIDE'),
    (r'\d+', 'NUMBER'),  # Números enteros
    (r'\d+\.\d+', 'FLOAT'),  # Números de punto flotante
    (r'[a-zA-Z_]\w*', 'IDENTIFIER'),  # Identificadores
]

# Código fuente de ejemplo
source_code = """
int main() {
    int x = 5;
    float y = 3.14;
    if (x > 0) {
        y = y * 2;
    } else {
        y = y / 2;
    }
    return 0;
}
"""

# Función de análisis léxico
def tokenize(code):
    token_list = []
    while code:
        for pattern, token_type in tokens:
            match = re.match(pattern, code)
            if match:
                value = match.group(0)
                token_list.append((value, token_type))
                code = code[len(value):].lstrip()
                break
        else:
            raise Exception(f"No se pudo analizar el token en: {code}")
    return token_list

# Ejecutar el análisis léxico
tokens = tokenize(source_code)

# Imprimir los tokens resultantes
for token in tokens:
    print(f"Token: {token[0]}, Tipo: {token[1]}")

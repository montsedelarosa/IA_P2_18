# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

class Program:
    def __init__(self, statements):
        self.statements = statements

class Assignment:
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

class Variable:
    def __init__(self, name):
        self.name = name

class Number:
    def __init__(self, value):
        self.value = value

def check_types(node, symbol_table):
    if isinstance(node, Program):
        for statement in node.statements:
            check_types(statement, symbol_table)
    elif isinstance(node, Assignment):
        variable_name = node.variable.name
        if variable_name not in symbol_table:
            print(f"Error semántico: Variable '{variable_name}' no declarada")
        else:
            expected_type = symbol_table[variable_name]
            expression_type = infer_type(node.expression, symbol_table)
            if expected_type != expression_type:
                print(f"Error semántico: Tipos no coinciden en la asignación de '{variable_name}'")
    elif isinstance(node, Number):
        # Los números tienen un tipo int o float
        return int if isinstance(node.value, int) else float

# Crear un programa AST de ejemplo
symbol_table = {'x': int, 'y': float}
program = Program([
    Assignment(Variable('x'), Number(10)),
    Assignment(Variable('y'), Number(3.14)),
    Assignment(Variable('z'), Number(42)),  # Esto generará un error
])

# Verificar los tipos del programa
check_types(program, symbol_table)

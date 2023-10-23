# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# Gramática de Tipo 0
grammar_type_0 = {
    "S -> aSb | ab": 1
}

# Gramática de Tipo 1
grammar_type_1 = {
    "aAb -> aaB": 1,
    "aAa -> aa": 1,
    "Ba -> aB": 1,
    "Ba -> ab": 1,
    "Ba -> bB": 1,
    "Ba -> bb": 1
}

# Gramática de Tipo 2
grammar_type_2 = {
    "S -> aS | bS | ε": 1
}

# Gramática de Tipo 3
grammar_type_3 = {
    "S -> aA | bB": 1,
    "A -> a | ε": 1,
    "B -> b | ε": 1
}

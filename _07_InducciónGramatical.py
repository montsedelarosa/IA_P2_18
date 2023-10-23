# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install nltk

import nltk
from nltk import Nonterminal, nonterminals, Production, CFG

# Ejemplos de oraciones
sentences = [
    "El gato come pescado.",
    "Los perros ladran fuerte.",
    "El pájaro canta en la mañana.",
]

# Tokenización de las oraciones
tokens = [nltk.word_tokenize(sentence) for sentence in sentences]

# Creación de la gramática inductiva
start_symbol = Nonterminal('S')
grammar = CFG(start_symbol, [])

for tokenized_sentence in tokens:
    production = Production(start_symbol, tokenized_sentence)
    grammar.productions().append(production)

# Mostrar la gramática resultante
print(grammar)

# Ejemplo de análisis sintáctico con la gramática inductiva
parser = nltk.ChartParser(grammar)
for tokenized_sentence in tokens:
    for tree in parser.parse(tokenized_sentence):
        tree.pretty_print()

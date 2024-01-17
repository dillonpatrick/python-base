#!/usr/bin/env python3
"""Calculadora prefix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefix_calc.py sum 5 2
7

$ prefix_calc.py mul 10 5
50

$ prefix_calc.py
operação: sum
n1: 5
n2: 4
9
"""

__version__ = "0.1.0"
__author__ = "Dillon"

import sys

arguments = sys.argv[1:]


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

valid_ops = {
    "sum": (num1 + num2),
    "sub": (num1 - num2),
    "mul": (num1 * num2),
    "div": (num1 / num2),
}

valid_ops_keys = list(valid_ops.keys())

ops_selected = input(f"Selecione um operação válida:\n {valid_ops_keys}\n").lower()

if ops_selected not in valid_ops:
    print("Invalid Operation")
    print(valid_ops_keys)
    sys.exit(1)
result = valid_ops[ops_selected]

print(f"Resultado: {result}")

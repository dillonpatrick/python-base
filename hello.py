#!/usr/bin/env python3

"""Tabuada do 1 ao 10"""

__version__ = "0.1.0"
__author__ = "Dillon Patrick"

numeros = list(range(1, 11))

for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        multiplication = numero * outro_numero
        print(f"{numero} x {outro_numero} = {multiplication}")

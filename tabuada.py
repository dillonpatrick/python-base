#!/usr/bin/env python3

"""Tabuada do 1 ao 10"""

__version__ = "0.1.0"
__author__ = "Dillon Patrick"

numeros = list(range(1, 11))

for n1 in numeros:
    print("{:#^18}".format(f"Tabuada do {n1}"))
    for n2 in numeros:
        calculo = n1 * n2
        print("{:-^18}".format(f"{n2} x {n2} = {calculo}"))
    print("*" * 18)

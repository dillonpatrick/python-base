#!/usr/bin/env python3

"""Comentarios multilinha
Geralmente usados para dar instruções de execução do codigo
"""
__version__ = "0.0.1"
__author__ = "Dillon Patrick"
__licence__ = "Unlicense"

import os

current_language = os.getenv("LANG", "us_US")[:5]

msg = "Hello World"

if current_language == "pt_BR":
    msg = "Ola Mundo"
elif current_language == "it_IT":
    msg = "Ciao Mondo"

print(msg)

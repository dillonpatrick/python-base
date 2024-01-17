#!/usr/bin/env python3
"""
Script que pergunte ao usuario qual a temperatura atual e o indice de umidade do ar sendo que caso sera exibida um mensagem de alerta dependendo das condições:

temp maior 45: Alerta!!! Perigo calor extremo
temp vezes 3 for maior ou igual a umidade: Alerta!!! Perigo de calor umido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
tem <0: Alerta: Frio extremo
"""
import sys
import logging

log = logging.Logger("alerta")

info = {"temperatura": None, "umidade": None}

keys = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"Qual a {key} atual?\n").strip())
    except ValueError:
        log.error(f"{key.capitalize()} invalida")
        sys.exit(1)

temperatura = info["temperatura"]
umidade = info["umidade"]

if temperatura > 45:
    print(f"Alerta!!! Perigo de calor extremo: {temperatura}ºC,Umidade: {umidade}%")

elif temperatura * 3 >= umidade:
    print(f"Alerta!!! Perigo de calor umido: {temperatura}ºC, Umidade: {umidade}%")

elif temperatura >= 10 and temperatura <= 30:
    print(f"Normal: {temperatura}ºC, Umidade: {umidade}%")

elif temperatura >= 0 and temperatura <= 10:
    print(f"Frio: {temperatura}ºC, Umidade: {umidade}%")

elif temperatura < 0:
    print(f"Alerta!!! Perigo de frio extremo: {temperatura}ºC, Umidade: {umidade}%")

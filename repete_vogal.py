#!/usr/bin/env python3
"""
Repete vogais
Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.
ex:
python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo
 
"""


def duplica_vogais(word):
    new_word = ""
    for letter in word:
        # TODO: Remover acentuação usando função
        if letter.lower() in "aeiou":
            new_word += letter * 2
        else:
            new_word += letter
    return new_word


while True:
    word = input("Digite uma palavra (ou pressione Enter para sair): ").strip()
    if not word:
        break
    resultado = duplica_vogais(word)
    print(f"Saída: {resultado}")

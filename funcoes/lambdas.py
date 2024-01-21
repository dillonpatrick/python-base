#!/usr/bin/env python3

"""
Algumas regras:

A função lambda pode receber argumentos
A função lambda não pode retornar valor
A função lambda não DEVE ser definida como variável
A função lambda não pode ter mais de uma expressão
"""

names = ["Dillon", "Celina", "Jhow", "Allan", "Alanna", "Irineu", "Amanda", "Kethelin"]


print(sorted(names, key=lambda name: name.count(("i"))))

print(list(filter(lambda name: name[0].lower() == "a", names)))

print(list(map(lambda name: "Hello " + name, names)))

# calculadora
print("-" * 30)
operacao = input("Operacao [sum, mul, div, sub]:").strip()
n1 = input("n1:").strip()
n2 = input("n2:").strip()


operacoes = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}


resultado = operacoes[operacao](int(n1), int(n2))

print(f"O resultado é: {resultado}")

nome = "dillon"
print((lambda n: f"hello {n}")(nome))

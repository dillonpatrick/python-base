"""Exemplos de funções"""

"""
f(x) = 5 * (x / 2)
"""


def f(x):
    result = 5 * (x / 2)
    return result


def print_in_upper(text):
    print(text.upper())


def heron(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s - b) * (s - c)
    return area ** (0.5)


triangulos = [(1, 23, 4), (2, 4, 6), (4, 7, 1), (6, 9, 2), (1, 11, 23), (5, 77, 2.5)]

for t in triangulos:
    area = heron(*t)
    print(area)

triangulo = heron(2, 4, 5)
print(triangulo)

valor = f(4.3)
print(valor)

print_in_upper("dillon")

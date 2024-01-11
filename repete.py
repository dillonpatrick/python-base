#!/usr/bin/env python3


numbers = range(1, 101)

for number in numbers:
    par = number % 2 == 0
    if par:
        print(number)
    else:
        continue
    print("mais codigo", number)

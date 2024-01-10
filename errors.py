#!/usr/bin/env python3
import os
import sys

try:
    names = open("names.txt").readlines()
except Exception as e:  # Bare except
    print(f"{str(e)}")
    sys.exit(1)
    # TODO: Usar o retry
else:
    print("Sucesso!!!")
finally:
    print("Executa isso sempre")


try:
    print(names[2])
except Exception as e:  # Bare except
    print(f"{str(e)}")
    sys.exit(1)

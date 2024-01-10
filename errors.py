#!/usr/bin/env python3
import os
import sys

if os.path.exists("names.txt"):
    print("O arquivo existe")
    input("...")
    names = open("names.txt").readlines()
else:
    print("[Error] File 'names.txt' not found.")

if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in the list.")
    sys.exit(1)

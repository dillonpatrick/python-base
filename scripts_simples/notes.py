#!/usr/bin/env python3

"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text:
Anotação geral sobre carreira de tecnologia

$notes.py read --tag=tech
...
...
"""

__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")
cmds = ("read", "new")


arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"you must specify subcomamnd {cmds}")

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print(f"-" * 30)
            print()


if arguments[0] == "new":
    try:
        title = arguments[1]
        text = [
            f"{title}",
            input("tag:").strip(),
            input("text:\n").strip(),
        ]
    except Exception as e:
        print(f"{str(e)}")
        sys.exit(1)

    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")

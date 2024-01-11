#!/usr/bin/env python3


dados = {}
for line in open("post.txt"):
    if "---" in line:
        break
    key, value = line.split(":")
    dados[key] = value.strip()
print(dados)

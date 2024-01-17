#!/usr/bin/env python3

import os
import sys

arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except Exception as e:
        # TODO: logging
        print(f"[ERROR] {str(e)}")
        print("You need to use '='")
        print(f"You passed {arg}")
        print("try with --key=value")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Opetaion `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]

if current_language is None:
    # TODO: Usar repetições
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
}

print(msg[current_language] * int(arguments["count"]))

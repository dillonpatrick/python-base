#!/usr/bin/env python3

import os

current_language = os.getenv("LANG", "en_US")[:5]


msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
}

if current_language not in msg:
    print("LANG atual:", current_language)
else:
    print(msg[current_language])

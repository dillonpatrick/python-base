#!/usr/bin/env python3
import smtplib

SERVER = "localhost"
PORT = 8025

""" Exemplors de envio de e-mail"""
FROM = "dillonti@outlook.com"
TO = ["destino1@server.com", "destino2@server.com"]
SUBJECT = "Meu e-mail via python"
TEXT = """\
Este é o meu e-mail eniado pelo python
<b>Olá Mundo</b>
"""


# SMTP
message = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))

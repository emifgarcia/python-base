#!/usr/bin/env python3

"""Hello world multi linguas

Exibe a mensagem no idioma configurado da variável de ambiente.

Como usar:

Tenha a variavel LANG devidamente configurada:

	export LANG=pt_BR

Execucao:

	python3 hello.py
	ou
	./hello.py
"""


__version__ = "0.1.0"
__author__ = "Marcelo Garcia"
__licensa__ = "Unlicense"


import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, world!"

if current_language == "pt_BR":
	msg = "Olá, mundo!"
elif current_language == "it_IT":
	msg = "Ciao, mundo!"
elif current_language == "es_SP":
	msg = "Hola, mundo!"
elif current_language == "fr_FR":
	msg = "Bonjur, monde!"	

print(msg)


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


__version__ = "0.1.2"
__author__ = "Marcelo Garcia"
__licensa__ = "Unlicense"


import os

current_language = os.getenv("LANG", "en_US")[:5]


msg = {
	"pt_BR": "Olá, mundo!",
	"it_IT": "Caio, mundo!",
	"es_SP": "Hola, mundo!",
	"fr_FR": "Bonjur, mode!",
	"en_US": "Hello, world!",
}

print(msg[current_language])




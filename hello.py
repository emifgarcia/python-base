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


__version__ = "0.1.3"
__author__ = "Marcelo Garcia"
__licensa__ = "Unlicense"


import os
import sys

sys_argv = sys.argv[1:]

#definindo argumentos que o programa espera receber
arguments = {
	"lang": None,
	"count": 1,
}


for arg in sys_argv:
	#TO DO: tratar ValueError
	key, value = arg.split("=")
	key = key.lstrip("-").strip()
	value = value.strip()
	if key not in arguments:
		print(f"'{key}': Invalid options")
		sys.exit() #para a execução do programa
	arguments[key]=value


current_language = arguments["lang"]
if current_language is None:
	#TO DO: usar repetição
	if "LANG" in os.environ:
		current_language = os.getenv("LANG")	
	else:
		current_language = input("Choose a language: ")

current_language = current_language[:5]

msg = {
	"pt_BR": "Olá, mundo!",
	"it_IT": "Caio, mundo!",
	"es_SP": "Hola, mundo!",
	"fr_FR": "Bonjur, mode!",
	"en_US": "Hello, world!",
}

print(msg[current_language] * int(arguments["count"]))




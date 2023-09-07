#!/usr/bin/env python3


"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.

Aula Inglês:
Sala 1: Erick, Maia, Joana
Sala 2: Carlos, Antonio

Aula Música:
Sala 1: Erick
Sala 2: Carlos, Maria

Aula Dança:
Sala 1: Gustavo, Sofia, Joana
Sala 2: Antonio

"""


__version__ = "0.1.0"
__author__ = "Marcelo Garcia"
__license__ = "unlicense"

#dados
sala1 = ["Erick", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erick", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erick", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

# listar alunos em cada atividade por sala
alunos_atividade_sala1 = []
alunos_atividade_sala2 = []

for aluno in aula_ingles:
	if aluno in sala1:
		alunos_atividade_sala1.append(aluno)
	elif aluno in sala2:
		alunos_atividade_sala2.append(aluno)
print("Aula Inglês:")
print("Sala 1:", alunos_atividade_sala1)
print("Sala 2:", alunos_atividade_sala2)
alunos_atividade_sala1.clear()
alunos_atividade_sala2.clear()

for aluno in aula_musica:
	if aluno in sala1:
		alunos_atividade_sala1.append(aluno)
	elif aluno in sala2:
		alunos_atividade_sala2.append(aluno)
print("Aula Música:")
print("Sala 1:", alunos_atividade_sala1)
print("Sala 2:", alunos_atividade_sala2)
alunos_atividade_sala1.clear()
alunos_atividade_sala2.clear()	

for aluno in aula_danca:
	if aluno in sala1:
		alunos_atividade_sala1.append(aluno)
	elif aluno in sala2:
		alunos_atividade_sala2.append(aluno)
print("Aula Dança:")
print("Sala 1:", alunos_atividade_sala1)
print("Sala 2:", alunos_atividade_sala2)	








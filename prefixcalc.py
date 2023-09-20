#!/usr/bin/env python3

""" Calculadora prefix.

Funcionamento:

Argumentos: [operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:

#Operação padrão:
$ prefixcalc.py
operação: sum
n1: 5
n2: 4
9.0

$ prefixcalc.py sum 5 2
7.0

$ prefixcalc.py mul 10 5
50.0

$ prefixcalc.py div 3
Invalid operation


"""

__version__ = "0.1.0"
__author__ = "Marcelo Garcia"
__license__ = "unlicense"



import sys

arguments = sys.argv[1:]

valid_arguments = ("sum", "sub", "mul", "div")

if not arguments:
	operation = input("operação: ").strip()
	if operation not in valid_arguments:
		print("Invalid arguments: invalid operation")
		sys.exit()
	n1 = input("n1: ")
	n2 = input("n2: ")
	arguments = [operation, n1, n2]

elif len(arguments) != 3:
	print("Invalid arguments: expected three arguments")
	sys.exit()
elif arguments[0] not in valid_arguments:
	print("Invalid arguments: invalid operation")
	sys.exit()

operation, *nums = arguments

validated_numbers = []
for num in nums:
	if not num.isdigit():
		print("Invalid arguments: arguments 2 and 3 must be numbers")
		sys.exit()
	elif num.isdigit():
		num = int(num)
		validated_numbers.append(num)

n1, n2 = validated_numbers

operations = {
	"sum": n1 + n2,
	"sub": n1 - n2,
	"mul": n1 * n2,
	"div": n1 / n2,
}

result = operations[operation]
print(result)


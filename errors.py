#! /usr/bin/env python3

import sys
import os

# EAFP - Easy to Ask Forgiveness than Permission 
# é mais fácil pedir perdão do que permissão


try:
	names = open("names.txt").readlines()
except (FileNotFoundError, ZeroDivisionError) as e:
	print(f"[Error] {str(e)}")
	sys.exit(1)
else:
	print("Sucesso!")

finally:
	print("execute isso sempre")

try: 
	print(names[0])
except:
	print("[Error] Missing name in the list")
	sys.exit(1)
#! /usr/bin/env python3

import sys
import os

if os.path.exists("names.txt"):
	print("File exists")
	input("...") # race conditional
	names = open("names.txt").readlines()
else:
	print("[Error] file 'names.txt' not found")
	sys.exit(1)


if len(names) >= 3:
	print(names[2])
else:
	print("[Error] Missing name in the list")
	sys.exit(1)
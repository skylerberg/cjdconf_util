#!/usr/bin/env python
import json
import sys

def read_file(filename):
	with open(filename) as f:
		contents = f.readlines()
	contents =  "".join(contents)
	return json.loads(contents)


def main():
	a = read_file(sys.argv[1])
	pulic_key = a["publicKey"]
	password = a["admin"]['password']
	bind = a["admin"]['bind']
	print bind
if __name__=="__main__":
	main()

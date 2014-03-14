import sys
import json

f = open(sys.argv[1],"r+w")
lines = f.readlines()
for line in lines:
	if not line.lstrip().startswith('//'):
		f.write(line)
		print line
f.close()

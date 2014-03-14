#!/usr/bin/env python
import sys
import json

def read_file(filename):
    preprocess(filename)
    with open(filename) as f:
        contents = f.readlines()
    contents =  "".join(contents)
    return json.loads(contents)

def preprocess(filename):
    outlines = list()
    f = open(filename)
    lines = f.readlines()
    in_multiline_comment = False
    for line in lines:
        if "/*" in line:
            in_multiline_comment = True
        if not line.lstrip().startswith('//') and not in_multiline_comment and line.strip() != "":
            outlines.append(line)
        if "*/" in line:
            in_multiline_comment = False
    f.close()
    f = open(filename,"w")
    f.write("".join(outlines))
    f.close()

def main():
    preprocess(sys.argv[1])

if __name__ == "__main__":
    main()

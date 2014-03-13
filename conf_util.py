#!/usr/bin/env python
import json
import sys

def read_file(filename)
    with open(filename) as f:
        contents = f.read()
    return json.loads(contents)

def main():
    read_file(sys.argv[1])

if __name__ == "__main__":
    main()

#!/usr/bin/env python
import json
import sys

from preprocess import read_file

def main():
    if len(sys.argv) != 3:
        print "Requires two arguments: a configuration file and a file containing json with the necessary information to add a peer."
        exit(1)
    conf = read_file(sys.argv[1])
    info = read_file(sys.argv[2])

    conf["authorizedPasswords"].append({"password": info["password"]})
    conf["interfaces"]['UDPInterface'][0]['connectTo'][info["ip"] + ":" + info["port"]] = {"password":info["password"], "publicKey":info["publicKey"]}
    with open(sys.argv[1],"w") as out:
        out.write(json.dumps(conf, sort_keys=True, indent=4))

if __name__=="__main__":
    main()

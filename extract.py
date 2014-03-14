#!/usr/bin/env python
import json
import sys

from preprocess import read_file

def main():
    if len(sys.argv) != 3:
        print "Requires two arguments: a configuration file and your IP address."
        exit(1)
    conf = read_file(sys.argv[1])
    ip = sys.argv[2]
    public_key = conf["publicKey"]
    password = conf["authorizedPasswords"][0]['password']
    bind = conf["interfaces"]['UDPInterface'][0]['bind']
    port = bind[bind.find(':') + 1:]
    json_dict = {"password":password, "port":port, "publicKey":public_key, "ip":ip}
    print json.dumps(json_dict)

if __name__=="__main__":
    main()

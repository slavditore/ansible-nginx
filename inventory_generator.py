#!/usr/bin/env python3

import argparse
import configparser

# Create a list of command-line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-H", "--hosts", required=True,
   help="list of hosts, separated by commas")
ap.add_argument("-u", "--user", required=True, help="user name")
ap.add_argument("-k", "--keyfile", required=False, help="path to keyfile")
ap.add_argument("-p", "--password", required=False, help="sudo password")
args = vars(ap.parse_args())

inventory = configparser.ConfigParser(allow_no_value=True)
inventory['all:vars'] = {"ansible_ssh_user": str(args['user'])}
inventory['nginx'] = {}
if (args['keyfile']):
    inventory["all:vars"]["ansible_ssh_key"] = str(args["keyfile"])
if (args['password']):
    inventory["all:vars"]["ansible_become_pass"] = str(args["password"])
nginx_hosts = str(args["hosts"]).split(",")
for i in nginx_hosts:
    inventory['nginx'][str(i)] = None


with open('inventory.ini', 'w') as configfile:
    inventory.write(configfile)
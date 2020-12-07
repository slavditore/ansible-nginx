#!/bin/bash

echo "Enter sudo password"
read -s pass

echo "Generate an inventory"
./inventory_generator.py -H $1 -u $2 -k $3 -p $pass

echo "Starting the playbook"
ansible-playbook -i inventory.ini nginx-playbook.yml --check
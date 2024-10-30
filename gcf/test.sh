#!/bin/bash

set -euo pipefail 

source ~/git/app-mod-workshop-set-by-step/.env 

#echo "DB_USER=$DB_USER"
export DB_USER=$DB_USER 
export DB_PASS=$DB_PASS 
export DB_HOST=$DB_HOST 
export DB_NAME=$DB_NAME 

python test.py
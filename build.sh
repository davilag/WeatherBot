#! /bin/bash

#Checking if pip is installed.
hash pip3 2>/dev/null || { echo >&2 "I require pip3 but it's not installed.  Aborting."; exit 1; }

echo "Installing all dependencies..."

pip3 install -r requirements.txt

echo "All denpendencies installed!"

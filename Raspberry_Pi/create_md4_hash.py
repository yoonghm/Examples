#!/bin/bash

echo -n "Password: "
read -s password
echo
echo -n $password | iconv -t utf16le | openssl md4 | awk '{ print $2}'

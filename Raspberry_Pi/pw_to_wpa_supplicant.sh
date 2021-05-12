#!/bin/bash

# This script encrypts a password for WPA2 Enterprise
# and replace the "xxxx" in /etc/wpa_supplicant/wpa_supplicant.conf with 
# new encrypted password

(read -p "WPA2 Enterprise password: " -s pw; echo -n $pw ; pw="") |
iconv -t utf16le |
openssl md4 | cut -c10- |
xargs -I '{}' sudo sed -i 's/xxxx/{}/' /etc/wpa_supplicant/wpa_supplicant.conf

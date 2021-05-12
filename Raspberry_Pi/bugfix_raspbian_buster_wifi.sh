#!/bin/bash

#	There is an unresolved WiFi bug on in Raspberry Pi OS for Buster.
# The bug could be overcome by swapping "nl80211,wext" to "wext,nl80211" from these two files:
# -	/lib/dhcpcd/dhcpcd-hooks/10-wpa_supplicant and
# -	/etc/wpa_supplicant/functions.sh

sudo sed -i 's/nl80211,wext/wext,nl80211/g' /lib/dhcpcd/dhcpcd-hooks/10-wpa_supplicant /etc/wpa_supplicant/functions.sh

#!/usr/bin/env python3

## Description
# Send a broadcast message to port=port in its current network
#
import socket
import ipaddress

# Broadcast address is obtained by combining:
# network address part and inverse of netmask
# E.g. IP = 192.168.56.1 Netmask = 255.255.255.0
# Then Network   address = 192.168.56.  0
#    Inversed of netmask =   0.  0. 0.255
#      Broadcast address = 192.168.56.255
# Use ipaddress standard library to do the work

port      = 12345
netmask   = '255.255.255.0'

hostname  = socket.gethostname()
ip        = socket.gethostbyname(hostname)

net       = ipaddress.IPv4Network(ip + '/' + netmask, False)
broadcast = str(net.broadcast_address)

print('Hostname          : {}'.format(hostname))
print('IP Address        : {}'.format(ip))
print('Broadcast Address : {}'.format(broadcast))

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set it to broadcast at SOL_SOCKET level to 1
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Send byte of strings to destination
sock.sendto(b'Hello world', (broadcast, port))

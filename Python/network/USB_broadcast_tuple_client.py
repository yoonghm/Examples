#!/usr/bin/env python3

## Description
# Broadcast a tuple to port=port in its current network
#

import socket
import time
import struct
import random

import msg_struct

port      = 12345
netmask   = '255.255.255.0'

hostname  = socket.gethostname()
ip        = socket.gethostbyname(hostname)
print('Hostname          : {}'.format(hostname))
print('IP Address        : {}'.format(ip))

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set it to broadcast at SOL_SOCKET level to 1
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

for i in range(0, 25):
  msg = struct.pack(msg_struct.tMsg,
                    int(time.time()),
                    i,
                    random.random(),
                    'Hello world {:>3d}'.format(i).encode()
                    )
  # Broadcast the message the local network
  sock.sendto(msg, ('<broadcast>', port))

  time.sleep(1)

# Close socket
sock.close()

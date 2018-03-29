#!/usr/bin/env python3

## Description
# Listen and display first connection to port=port from any address
#

import socket

port = 12345

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Listen to all address to port=port
sock.bind(('', port))

# Wait for the first connection to buffer of 1024 bytes
bytes, address,  = sock.recvfrom(1024)

print('Received {0} from {1}:{2}'.format(bytes, address[0], address[1]))

# Close socket
sock.close()


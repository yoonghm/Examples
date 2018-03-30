#!/usr/bin/env python3

## Description
# Listen and display first connection to port=port from any address
# The program exit if any condition below is true
#  a) There is no activity for 'timeout' seconds during recvform()
#  b) It receive a message with index 'exitidx'
#

import socket
import time
import struct

import msg_struct

port = 12345
timeout = 60
exitidx = 20

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Listen to port `port` at addresses
sock.bind(('', port))

# Set timeout to `timeout` seconds if there is no activity
sock.settimeout(timeout)

while True:
  msg, address = sock.recvfrom(struct.calcsize(msg_struct.tMsg))
  if msg:
    (tm_, idx_, val_, str_) = struct.unpack(msg_struct.tMsg ,msg)
    print('{0} {1}: {2} {3:>3d} {4:<4.3f} "{5}"'.format(
            time.strftime('%Y-%m-%d %H:%M:%S'),
            address[0],
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(tm_)),
            idx_,
            val_,
            str_.decode().replace('\x00','')
            )
         )
    if (idx_ == exitidx):
      break

# Close socket
sock.close()

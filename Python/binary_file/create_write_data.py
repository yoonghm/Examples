#!/usr/bin/env python3

import os
import struct
import errno
import sys

s = struct.Struct('q8sfxxxx')

db = [(1, b'Hong Hua', 2000.0),
      (2, b'Ali Mohd', 2000.0),
      (1, b'Ravi Abu', 2200.0),
     ]

fd = os.open('./database.db', os.O_RDWR|os.O_CREAT|os.O_TRUNC)
if (fd < 0):
  print('write(): error')
  sys.exit(-1)

for i in range(len(db)):
  pack = s.pack(*db[i])
  ret = os.write(fd, pack)
  if (ret != s.size):
    print("write error")
    os.close(fd)
    sys.exit(-1)

os.close(fd)
sys.exit(0)

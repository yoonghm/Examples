#!/usr/bin/env python3

import os
import struct

x = struct.Struct('q8sfxxxx')

fd = os.open('./database.db', os.O_RDONLY)
while True:
  buf = os.read(fd, x.size)
  if len(buf) == x.size:
    rec = x.unpack_from(buf)
    print(rec)
  else:
    break

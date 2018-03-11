#!/usr/bin/env python3

import os
import struct

s = struct.Struct('q8sfxxxx')
rec = (4, b'Tze Kong', 3200.0)
pack = s.pack(*rec)

fd = os.open('./database.db', os.O_RDWR)

# Move pointer to the end
os.lseek(fd, 0, os.SEEK_END)
n = os.write(fd, pack)
if (n != s.size):
	print("write error")

os.close(fd)

#!/usr/local/env python3

import struct

fmt = 'h ? i f q d 8s'
print(fmt, 'uses', struct.calcsize(fmt), 'bytes')

data = (12,
        True,
        123,
        3.1415,
        99999999,
        9239193193.23123,
        b'hello123'
       )

pack = struct.pack(fmt, *data)
print('pack   =', pack)
print('unpack =', struct.unpack(fmt, pack))

#!/usr/bin/env python3

import struct

fmt1 = 'h i q f d ? 8s'

print(fmt1, 'uses', struct.calcsize(fmt1), 'bytes')

data = (12,                          # short     2
        123,                         # integer   4
        99999999,                    # long long 8
        3.1415,                      # float     4
        9239193193.231232313123,     # double    8
        True,                        # bool      1
        b'hello123'                  # char[])   8
        )

pack1 = struct.pack(fmt1, 
                    12,
                    123,
                    99999999,
                    3.1415,
                    9239193193.231232313123,
                    True,
                    b'hello123'
                   )

# Alternatively, use a shorter format
pack1a = struct.pack(fmt1, *data)

# Let's check their contents
print('pack1  = ', pack1)
print('pack1a = ', pack1a)

# Re-arrange the data to maximize packing
fmt2 = 'h ? i f q d 8s'

print(fmt2, 'uses', struct.calcsize(fmt2), 'bytes')

pack2 = struct.pack(fmt2,
                    12,
                    True,
                    123,
                    3.1415,
                    99999999,
                    9239193193.231232313123,
                    b'hello123'
                   )

# Let's print its content
print('pack2  = ', pack2)

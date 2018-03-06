#!/usr/local/env python3
import struct

print(struct.calcsize('h i'))  # 2 _ _ 4 = 8
print(struct.calcsize('i h'))  # 4 2     = 6

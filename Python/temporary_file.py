#!/usr/bin/env python3

from tempfile import mkstemp
import os

fd, path = mkstemp(prefix='python',suffix='.db')
# A temporary file is created and opened for RW+Binary

# os.write is system low-level write function which take bytes
os.write(fd, b'This is string 1\n')        # 17 bytes
os.write(fd, '你好世界\n'.encode('utf8'))   # 13 bytes
os.write(fd, b'This is string 3\n')        # 17 bytes

os.close(fd)                               # Close the file
fd = os.open(path, os.O_RDWR)              # Re-open the file
                                           # File ptr is at 0th byte

os.lseek(fd, 17, os.SEEK_SET)              # Move file ptr to 17th byte
print(os.read(fd, 13).decode())            # print 你好世界


os.lseek(fd, 0, os.SEEK_SET)               # Move file ptr to head

                                           # Read by chunk
while True:
  data = os.read(fd, 1024)
  if not data:
    break
  print(data.decode())

os.close(fd)                               # Close the file

input('Press ENTER to continue...')        # Wait for ENTER key

os.remove(path)                            # Delete the file

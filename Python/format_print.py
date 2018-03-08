#!/usr/bin/env python3

a = 123.456
b = 1.23456
c = -1.0

print(a, b, b*c)
print(a, b, b*c, sep=", ")
print(a, b, b*c, sep="      ")
print()

print('%.1f %.1f %.1f'    % (a, b, b*c))
print('%8.1f %8.1f %8.1f' % (a, b, b*c)) # 8 includes '.', '-'
print('%3.1f %3.1f %3.1f' % (a, b, b*c)) # width is shorter than value
print('%6.2e %6.2e %6.2e' % (a, b, b*c)) # exponential
print()

print("%08.2f" % 1.23)
print()

print("%x" % 100)
print("%X" % 100)
print("%#x" % 100)
print("%o" % 100)
print("%#o" % 100)
print("%+2d" % 100)
print("%+8d" % 100)

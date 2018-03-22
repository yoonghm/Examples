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
print()

str = '1th => {0}, 2th => {1}'.format(10, 99);            print(str)
str = '1th => {1}, 2th => {0}'.format(10, 99);            print(str)
str = '1th => {0:3.2f}, 2th => {1:3.2f}'.format(10, 99);  print(str)
str = '1th => {1:5.2E}, 2th => {0:5.2E}'.format(10, 99);  print(str)
print()

str = '{0:<20s}: ${1:6.2f}'.format('Eggs',   0.20);       print(str)
str = '{0:<20s}: ${1:6.2f}'.format('Mutton', 18.50);      print(str)
print()

str = '{0:>20s}: ${1:<6.2f}'.format('Eggs',   0.20);      print(str)
str = '{0:>20s}: ${1:<6.2f}'.format('Mutton', 18.50);     print(str)
print()

str = '{0:>20s}: ${1:>12,}'.format('Watch',   360);       print(str)
str = '{0:>20s}: ${1:>12,}'.format('House', 123456789);   print(str)
print()

str = '{0:>20s}: ${1:<12,}'.format('Watch',   360);       print(str)
str = '{0:>20s}: ${1:<12,}'.format('House', 123456789);   print(str)
print()

print('This is {grade}.'.format(grade='good'))

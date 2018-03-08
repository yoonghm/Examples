#!/usr/bin/env python3

from sys import getsizeof, float_info

def show(var):
   print('a =', var)
   print('    is', type(var), 'and occupies', getsizeof(var), '\n')

a = None;                         show(a)
a = True;                         show(a)
a = 1;                            show(a)
a = 1234567890;                   show(a)
a = 12345678901234567890;         show(a)
a = 0.1;                          show(a)
a = float_info.max;               show(a)
a = 1 + 2j;                       show(a)
a = 'a';                          show(a)
a = 'ab';                         show(a)
a = 'abc';                        show(a)
a = (1);                          show(a)
a = (1,);                         show(a)
a = (1, 2);                       show(a)
a = (1, 2, 3);                    show(a)
a = ("a", "b");                   show(a)
a = (1, "a");                     show(a)
a = (1, (1,2));                   show(a)
a = [1];                          show(a)
a = [1,2];                        show(a)
a = {'x':1};                      show(a)
a = {'x':1, 'y':2};               show(a)
a = {'x':1, 'y':2, 'z':3};        show(a)
a = set(["Access"]);              show(a)
a = set(["a", "b", "c", "a"]);    show(a)
a = set(("a", "b", "c", "a"));    show(a)

#/usr/bin/env python3

import datetime

name = 'Fred'
age = 50
anniversary = datetime.date(1991, 10, 12)
print(\
f'My name is {name}, \n\
My age next year is {age+1}. \n\
My anniversary is {anniversary:%A, %B %d, %Y}.'\
)

'''
My name is Fred, 
My age next year is 51. 
My anniversary is Saturday, October 12, 1991.
'''

#!/usr/bin/env python3

from datetime import datetime, timedelta

tmfmt = '%Y-%m-%d %M:%S'

print('-'*72)
now = datetime.now()
due = now + timedelta(days=1)

print(f'Now is {now.strftime(tmfmt)}')
print(f'Due on {due.strftime(tmfmt)}')
'''
Now is 2018-04-07 55:19
Due on 2018-04-08 55:19
'''

print('-'*72)
'''
Test Unix Millenium bug. 
Unix/Linux uses 32-bit integer to present seconds since 1972-1-1 00:00
'''

epoch =datetime(year=1970, month=1, day=1, minute=0, second=0)
print(epoch)
'''
1970-01-01 00:00:00
'''

new_date = epoch + timedelta(seconds=2**31 + 1)
print(new_date)
'''
2038-01-19 03:14:09
'''

print('-'*72)
'''
Compare time
'''

MAX_HOURS = timedelta(hours=10) # maximum 10 hours
curr_hours = timedelta() # 0:00
sp = ''

print(f'Countdown for {MAX_HOURS}\n')
while curr_hours < MAX_HOURS:
  print(f'{sp}Waiting for 1 hour ...')
  curr_hours += timedelta(hours=1)
  sp += ' '

print(f'Timeout. {MAX_HOURS} has passed.')

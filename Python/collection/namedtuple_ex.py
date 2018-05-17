from collections import namedtuple as nt

Tran = nt('Tran', 'fr, to, va, da, ga')

tr1 = Tran(fr=111, to=222, va=3, da='msg1', ga=0.1)
tr2 = Tran(fr=111, to=333, va=2, da='msg2', ga=0.1)
tr3 = Tran(fr=222, to=333, va=1, da='msg3', ga=0.1)
tr4 = Tran(fr=333, to=111, va=1, da='msg4', ga=0.1)

Trans = {}
Trans['1111111111'] = tr1
Trans['2222222222'] = tr2
Trans['3333333333'] = tr3
Trans['4444444444'] = tr4

print(Trans)

print('-' * 70)

print(Trans['1111111111'])

print('-' * 70)

sum = 0
person = 111
for t in Trans:
  if Trans[t].fr == person:
    sum += Trans[t].va

print(f'{person} has transferred {sum}')

'''
{'1111111111': Tran(fr=111, to=222, va=3, da='msg1', ga=0.1), '2222222222': Tran(fr=111, to=333, va=2, da='msg2', ga=0.1), '3333333333': Tran(fr=222, to=333, va=1, da='msg3', ga=0.1), '4444444444': Tran(fr=333, to=111, va=1, da='msg4', ga=0.1)}
----------------------------------------------------------------------
Tran(fr=111, to=222, va=3, da='msg1', ga=0.1)
----------------------------------------------------------------------
111 has transferred 5
'''

#!/usr/bin/env python3

str = 'hello world!'
print(str[0:5])
print(str[0:8:2])
print(str[::-1])      # Reverse the whole string
print(str[0:5][::-1]) # Reverse a substing
print()

str2 = "世界你好"
print(str2[::-1])

print(str, '.upper() gives',      str.upper())
print(str, '.lower() gives',      str.lower())
print(str, '.capitalize() gives', str.capitalize())
print(str, '.title() gives',      str.title())
print()

print(str.center(80).title())
print()

print('"h" is at ',     str.find('h'    ), 'th of "', str,'"', sep="")
print('"world" is at ', str.find('world'), 'th of "', str,'"', sep="")
print('"would" is at ', str.find('would'), 'th of "', str,'"', sep="")
print()
print(str, ".replace('hello', 'hi') gives", str.replace('hello', 'hi'))
print()

str3 = '''轻轻的我走了，正如我轻轻的来；我轻轻的招手，作别西天的云彩
'''
print('str3 =', str3)
print('first "轻轻" is at', str3.find('轻轻'))
print('last  "轻轻" is at', str3.rfind('轻轻'))
print()

str4 = 'Mobile:9999888'
_, _, mobile = str4.rpartition(':')
print('str4 =', str4)
print('mobile =', mobile)
print()

str5 = 'ID:Name:Company:Address:Postcode:Country'
print('Field-separated data:', str5)
fields = str5.rsplit(':')
print('2nd field =', fields[1])
print('4th field =', fields[3])
print()


#!/usr/bin/env python3

str = "Hello World!"
print(str, "has", len(str), "characters.")
print(str, "occupies", len(str.encode('utf8')), "bytes.")
print()

str = 'It says, "How are you today?"'
print(str)
print()

str = '''This is a very long text and spans several lines.
This is another line.
And, this is another line.
'''
print("str =", str)
print("str.splitlines() =", str.splitlines())
print()

# Unicode
# You may need to change the font that supports utf8
str = "世界你好"
print(str, "has", len(str), "characters.")
print(str, "occupies", len(str.encode('utf8')), "bytes.")

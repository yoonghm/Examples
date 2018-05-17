import json

data = '{"one" : "1", "two" : "2", "three" : "3"}'
j = json.loads(data)
print(j['two'])

'''
2
'''

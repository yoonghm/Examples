import json

data = '{"one" : "1", "two" : "2", "three" : "3"}'
j = json.loads(data)
print(j['two'])

class Student:
  def __init__(self, id, name, password):
    self.id = id
    self.name = name
    self.password = password

stud1 = Student(1,'Tan Ah Kau','123456')

# Convert Python object to JSON object
json1 = json.dumps(stud1.__dict__, separators=(',', ':'))
print(json)

j = json.loads('{"password": "222222", "id": 2, "name": "Bryan"}')
stud2 = Student(**j)

'''
2
{"password":"123456","id":1,"name":"Tan Ah Kau"}
'''

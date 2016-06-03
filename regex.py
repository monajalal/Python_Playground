import re
file = open('names.txt', 'r', encoding='utf-8')
names = file.read()
file.close()
print(names)
print(re.match(r'CEO', names)) #expect None
print(re.match(r'Love', names)) #expect a pointer
print(re.match(r'Vader', names))
print(re.search(r'Vader', names))
print(re.match(r'\w+, \w+', names))
print(re.search(r'\w+, \w+', names)) ###why?
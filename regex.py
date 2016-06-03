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
#why do I only get <_sre.SRE_Match object; span=(658, 670), match='555 555-5551'>
print(re.search(r'(\d{3}) \d{3}-\d{4}', names))
#why do I only get <_sre.SRE_Match object; span=(658, 669), match='555 555-555'>
print(re.search(r'(\d\d\d) \d\d\d-\d\d\d', names))
#got <_sre.SRE_Match object; span=(44, 58), match='(555) 555-5555'>
print(re.search(r'\(\d{3}\) \d{3}-\d{4}', names))
print(re.search(r'\(\d*\)',names))
print(re.search(r'\w+, \w+', names))
print(re.search(r'\(?\d*\)? \d{3}-\d{4}',names))
print(re.findall(r'\(?\d*\)? \d{3}-\d{4}',names))




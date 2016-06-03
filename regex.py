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
print(re.findall(r'\(?\d*\)?-?\s?\d{3}-\d{4}',names))
print(re.findall(r'\w*, \w+', names))


def phone_numbers(string):
    return re.findall(r'\d{3}-\d{3}-\d{4}', string)

def find_words(count, string):
    return re.findall(r'\w*count',string)

def check_email(string):
    return re.findall(r'[-\w\d+.]+@[-\w\d+.]+', string)
print(find_words(5, names))
print(check_email(names))
print(re.findall(r'[trehous]+', names, re.IGNORECASE))
print(re.findall(r'\b[trehous]+\b', names, re.I))
print(re.findall(r'\b[trehous]{9}\b', names, re.I))
print(re.findall(r'[trehous]{9}', names, re.I))

# Example:
# >>> find_email("kenneth.love@teamtreehouse.com, @support, ryan@teamtreehouse.com, test+case@example.co.uk")
# ['kenneth@teamtreehouse.com', 'ryan@teamtreehouse.com', 'test@example.co.uk']




print(re.findall(r'''
                  \b@
                  [\w\d+-.]*
                  [^gov\t]+
                  \b
                  ''', names, re.VERBOSE|re.I))

print(re.findall(r'''
                 \b[-\w ]*,
                 \s
                 [-\w ]+
                 [^\t\n]
                 ''', names, re.X|re.I))


string = 'Perotto, Pier Giorgio'
names = re.match(r'''
                 [-\w ]+, #first name
                 \s
                 [-\w ]+ #last name
                 ''',string, re.X|re.M)

print(names)

string = 'Perotto, Pier Giorgio'
names = re.findall(r'''
                 (?P<first>[-\w ]+),\s #first name
                 (?P<last> [-\w ]+) #last name
                 ''',string, re.X|re.M)

print(names)

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'''
                    (?P<email>[-\w+.]*@[-\w+.]+),
                    \s
                    (?P<phone>\d{3}-\d{3}-\d{4})
                     ''', string, re.X|re.M)

print(contacts)

twitters = re.search(r'''
                    (?P<handle>@[\w\d]+)$
                    ''', string, re.X|re.M)

print(twitters)

pattern = re.compile(r'''
                    (?P<handle>@[\w\d]+)$
                    ''', re.X|re.M)

print(re.search(pattern, string).groupdict())

def find_words2(count, string):
    return re.findall(r'\w' * count + r'\w*', string)

print(find_words2(3, "mona is a gooood girl"))

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'''
                     ^(?P<last_name>[-\w ]+),\s
                     (?P<first_name>[-\w ]+):\s
                     (?P<score>[\d]+)$
                     ''', string, re.M|re.X)
print(players)
print(players.groupdict())

def find_emails(string):
    return re.findall(r'[+\w.]*@[+\w.]+', string)

string = ''' De la Sota: Hello

Guini: Hello

Prat Gay: Hello
'''
print(re.findall(r'[-\w ]+[^:\sHelo]', string))
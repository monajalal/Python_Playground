'''
#>>> counts = dict()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict' object is not callable
'''


'''
>>> dict()
{}
>>> my_dict = dict()
>>> line = raw_input("hi?")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'raw_input' is not defined
>>> line = input("hi?")
hi?

'''

'''
>>> for word in ['red', 'blue', 'azure', 'red', 'blue', 'blue', 'yellow']:
...     cnt[word] += 1
... cnt
  File "<stdin>", line 3
    cnt
      ^
SyntaxError: invalid syntax
>>> print(cnt)
Counter()

'''
from collections import Counter
cnt = Counter()
for word in ['red', 'blue', 'azure', 'red', 'blue', 'blue', 'yellow']:
    cnt[word] += 1

print(cnt)
print(cnt.most_common())
print(cnt.most_common(2))
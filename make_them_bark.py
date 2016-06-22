'''
Can you solve this problem, or will you let this client outsmart you for good?

Practical info:

The .bark() method of a dog should return the string 'Woof!'.
The constructor you made (it is preloaded) looks like this:
class Dog(object):
    def __init__(self, name, breed, sex, age):
        self.name  = name
        self.breed = breed
        self.sex   = sex
        self.age   = age
Hint: A friend of yours just told you about how javascript handles classes differently
from other programming languages. He couldn't stop ranting about "prototypes", or
something like that. Maybe that could help you...
'''
#Doesn't pass codewars challenge

class Dog(object):
    def __init__(self, name, breed, sex, age):
        self.name  = name
        self.breed = breed
        self.sex   = sex
        self.age   = age


    def bark(self):
        return 'Woof'


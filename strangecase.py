#CodeWar Basic Challenges
def to_weird_case(string):
    #TODO
    new_string_arr = []
    string_arr = string.split()
    for word in string_arr:
        for i in range(len(word)):
            if i%2 == 0:
                new_string_arr.append(word[i].upper())
            else:
                new_string_arr.append(word[i].lower())
        new_string_arr.append(" ")
    return "".join(new_string_arr)


print(to_weird_case('This is a test'))

def vowel_indices(word):
    # your code here
    vowel_set = {'a', 'e', 'i', 'o', 'u', 'y'}
    vowel_index_list = []
    for i in range(len(word)):
        if word[i].lower() in vowel_set:
            vowel_index_list.append(i+1);
    return vowel_index_list

print(vowel_indices("Insane"))

'''
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
Test.assert_equals(get_sum(0,1),1)
Test.assert_equals(get_sum(0,-1),-1)
'''

def get_sum(a,b):
    #good luck!
    sum = 0
    if a < b :
        for i in range(a, b+1):
            sum += i
    elif a > b :
        for i in range(b, a+1):
            sum += i
    else:
        return a
    return sum

print(get_sum(-1,2))

'''
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive.
The string can contains any char.
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
Test.expect(xo('xo'))
Test.expect(xo('xo0'))
Test.expect(not xo('xxxoo'))
'''

def xo(s):
    x_count = 0
    o_count = 0
    for i in range(len(s)):
        if s[i].lower() == 'x':
            x_count += 1
        elif s[i].lower() == 'o':
            o_count += 1
    return x_count == o_count

print(xo("ooxXm"))
print(xo("xooxx"))

'''
Caesar Ciphers are one of the most basic forms of encryption.
It consists of a message and a key, and it shifts the letters
of the message for the value of the key.

Your task is to create a function encryptor that takes 2 arguments
 - key and message - and returns the encrypted message.

A message 'Caesar Cipher' and a key of 1 returns 'Dbftbs Djqifs'.

A message 'Caesar Cipher' and a key of -1 returns 'Bzdrzq Bhogdq'.

Make sure to only shift letters, and be sure to keep the cases of
the letters the same. All punctuation, numbers, spaces, and so on
should remain the same. Also be aware of keys greater than 26 and
less than -26. There's only 26 letters in the alphabet!
test.assert_equals(encryptor(13, ''), '')
test.assert_equals(encryptor(13, 'Caesar Cipher'), 'Pnrfne Pvcure')
test.assert_equals(encryptor(-5, 'Hello World!'), 'Czggj Rjmgy!')
test.assert_equals(encryptor(27, 'Whoopi Goldberg'), 'Xippqj Hpmecfsh')
'''
def encryptor(key, message):
    #Program me!
    if abs(key) > 26:
        key = key % 26
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']

    new_message_list = []
    for i in range(len(message)):
        if message[i].isalpha():
            char = alphabet[(alphabet.index(message[i].lower())+key)%26]
            if message[i].isupper():
                new_message_list.append(char.upper())
            else:
                new_message_list.append(char)
        else:
            new_message_list.append(message[i])
    return "".join(new_message_list)

print(encryptor(-5,"Hello World!"))
print(encryptor(27,"whoopi"))






'''
Your task is to write function which takes string and list of delimiters as
an input and returns list of strings/characters after splitting given string.

multiple_split('Hi, how are you?', [' ']) => # [Hi,', 'how', 'are', 'you?']
multiple_split('1+2-3', ['+', '-']) => ['1', '2', '3']
1, 3
'''

def multiple_split(string, delimiters=[]):
    if delimiters == [' ']:
        return string.split(' ')
    if delimiters == ['']:
        return string.split()
    if delimiters == None:
        return string
    index_array = []
    splitted_string = []
    for delimiter in delimiters:
        index_array.append(string.index(delimiter))
    if string[0] not in delimiters:
        splitted_string.append(string[0])
    for index in index_array:
        if index+1 not in delimiters:
            splitted_string.append(string[index+1])
    return splitted_string

print(multiple_split('1+2-3', ['+', '-']))
print(multiple_split('Hi, how are you?', [' ']))
print(multiple_split('Hi everybody!', [' ', '!']))


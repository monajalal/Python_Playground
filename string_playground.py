#find index of a string in another string
search_string = "hi"
string = "hello hi how are you?"
print(string.index(search_string))
sample="this is a string   "
result="_".join(sample.split())
print(result)
string2="abracadabra"
def replace_char(string, index, char):
    str_list = list(string)
    str_list[index] = char
    return "".join(str_list)
print(replace_char(string2, 5, 'k'))

""" hacker rank challenge https://www.hackerrank.com/challenges/python-mutations?h_r=next-challenge&h_v=zen
string2=input()
index_char=input().split()
index=int(index_char[0])
char=index_char[1]
def replace_char(string, index, char):
    str_list = list(string)
    str_list[index] = char
    return "".join(str_list)
print(replace_char(string2, index, char))
"""


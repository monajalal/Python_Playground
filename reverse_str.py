def FirstReverse(str):
    if len(str) == 0:
        return
    if len(str) == 1:
        return str
    reversed_str = ''
    for i in range(len(str)):
        reversed_str += str[len(str)-1-i]
    # code goes here
    return reversed_str


# keep this function call here
print(FirstReverse(input()))

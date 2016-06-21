'''
1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105
'''

def no_boring_zeros(n):
    # your code
    if n == 0:
        return n
    string_number = str(n)
    i = len(string_number) -1
    while (string_number[i] == '0'):
        i -= 1

    return int(string_number[0:i+1])

print(no_boring_zeros(-1050))






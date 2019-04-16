def SimpleSymbols(str):
    if len(str) < 1:
        return False
    if len(str) == 1 and str == '+':
        return True
    if str[0] != '+' and str[len(str)-1] != '+':
        return False

    for i in range(len(str)):
        if (str[i].isalnum() == False):
            if not (str[i] == '=' or str[i] == '+'):
                return False
    return True

print(SimpleSymbols("+d+=3=+s+"))


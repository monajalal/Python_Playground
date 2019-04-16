def AlphabetSoup(str):
    out = ''
    letters = sorted(list(str))
    for l in letters:
        out += l
    return out

print(AlphabetSoup('loldcb'))
'''
Write a function that takes a number or a string and gives back the number of
permutations without repetitions that can generated using all its element
'''

from itertools import permutations
def perms(object):
    string = str(object)
    perm_set = []
    perm_repeated = permutations(string)
    print(perm_repeated)

    perm_list = [''.join(p) for p in permutations(string)]
    for item in perm_list:
        if item not in perm_set:
            perm_set.append(item)
    return len(perm_set)


print(perms(737))




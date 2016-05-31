from itertools import permutations

for perm in permutations([1, 2, 3]):
    print(perm, end=" ")

print()


for perm in permutations("nice"):
    print("".join(perm), end=" ")

print()

for perm in permutations("mona"):
    print(perm, end=" ")
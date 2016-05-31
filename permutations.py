from itertools import permutations
"""
for perm in permutations([1, 2, 3]):
    print(perm, end=" ")

print()


for perm in permutations("nice"):
    print("".join(perm), end=" ")

print()

for perm in permutations("mona"):
    print(perm, end=" ")

print()
"""
def lexi_order(string, k):
    word_list = []
    for perm in permutations(string, k):
        word_list.append("".join(perm))
    for word in sorted(word_list):
        print(word)

#lexi_order("HACK", 2)

list = input()
print(list)
print(list[0])
print(list[1])
string = list[0]
k = int(list[1])
lexi_order(string, k)
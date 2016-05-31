from itertools import permutations

def lexi_order(string, k):
    word_list = []
    for perm in permutations(string, k):
        word_list.append("".join(perm))
    for word in sorted(word_list):
        print(word)

#lexi_order("HACK", 2)

list = input().split()
string = list[0]
k = int(list[1])
if (string.isupper() and k>0 and k<=len(string)):
    lexi_order(string, k)

for perm in permutations([1, 2, 3]):
    print(perm, end=" ")

print()


for perm in permutations("nice"):
    print("".join(perm), end=" ")

print()

for perm in permutations("mona"):
    print(perm, end=" ")




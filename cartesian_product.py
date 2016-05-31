from itertools import product
list1 = input().split()
list2 = input().split()
to_int = lambda x: map(int,x)

result = product(to_int(list1), to_int(list2))

for item in result:
    print(item, end=" ")

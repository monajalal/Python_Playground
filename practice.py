from collections import defaultdict

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1

print(d.items())

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
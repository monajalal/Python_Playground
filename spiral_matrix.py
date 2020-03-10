'''
expected input:
[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

expected output:
[1, 2, 3, 6, 9, 8, 7, 4, 5]

'''

b = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
#b = [[1, 2], [3, 4], [5, 6]]



#spiral type 1
# cols = len(a[0])
# rows = len(a)
# for j in range(rows):
#     for i in range(cols):
#             if (j % 2) == 0:
#                 print(a[j][i])
#             else:
#                 print(a[j][cols-i-1])


def spiral_matrix(m):
    result = []
    while len(m) > 0:
        result += m[0]
        m = list(zip(*m[1:len(m)]))[::-1]
    return result


print(spiral_matrix(b))

m = b
m = list(zip(*m[1:len(m)]))[::-1]
print(m)

m = b
m = list(zip(*m[0:len(m)]))
print(m)
s = 'mona'

print(s[::-1])

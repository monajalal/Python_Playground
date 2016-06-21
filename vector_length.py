'''
Test.assert_equals(vector_length([[0, 1],[0, 0]]), 1)
Test.assert_equals(vector_length([[0, 3],[4, 0]]), 5)
Test.assert_equals(vector_length([[1, -1],[1, -1]]), 0)
'''
import math

def vector_length(vector):
    x1 = vector[0][0]
    y1 = vector[0][1]
    x2 = vector[1][0]
    y2 = vector[1][1]
    return math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))

print(vector_length([[0, 1],[0, 0]]))

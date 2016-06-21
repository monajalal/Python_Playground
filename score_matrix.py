import math
def score_matrix(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sum += math.pow(-1, (i+j)) * matrix[i][j]
    return int(sum)

#print(score_matrix([[1, 2, 3], [-3, -2, 1], [3, -1, 2]]))
print(score_matrix([[1, 2, 3, 4], [-3, -2, 1, 1], [3, 8, -1, 2], [20, 5, 10, -4],
                   [10, -8, -8, 4]]))
print(score_matrix([[2,3,2,3], [2,3,2,3], [2,3,2,3]]))
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    sum_diag1 = 0
    sum_diag2 = 0
    arr_2d = []
    print(arr)

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                sum_diag1 += arr[i][j]
            elif i+j == (len(arr)) - 1:
                sum_diag2 += arr[i][j]
                print(arr[i][j])


    return abs(sum_diag1 - sum_diag2)




n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)

print(result)


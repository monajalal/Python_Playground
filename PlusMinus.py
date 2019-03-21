import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    negatives_count = 0
    zeros_count = 0
    positive_count = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            negatives_count += 1
        elif arr[i] == 0:
            zeros_count += 1
        else:
            positive_count += 1
    negatives_ratio = negatives_count/len(arr)
    zeros_ratio = zeros_count/len(arr)
    positive_ratio = positive_count/len(arr)

    #print(f'{negatives_ratio:.6f}') #python3.6
    #print(f'{zeros_ratio:.6f}') #python3.6
    #print(f'{positive_ratio:.6f}') #python3.6
    print(float("%.6f" % positive_ratio))
    print(float("%.6f" % negatives_ratio))
    print(float("%.6f" % zeros_ratio))


    return


n = int(input())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)

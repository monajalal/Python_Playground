def FirstFactorial(num):
    num = int(num)
    if num == 0 or num == 1:
        return 1
    elif num < 0:
        return
    else:
        # code goes here
        num = num * FirstFactorial(num - 1)
    return num


# keep this function call here
print(FirstFactorial(input()))
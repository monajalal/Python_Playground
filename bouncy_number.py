'''
Bouncy numbers
Problem 112
'''
def is_bouncy(num):
    #str_list = str(num).split()
    list_num = list(str(num))

    #return all(str_num[i] <= str_num[i+1] for i in range(len(str_num)-1))
    return not (sorted(list_num) == list_num) and  not (sorted(list_num) == list_num[::-1])
#1/100 (100)
#2/101 (101)
#3/103

# (num_bouncy(n-1)+ 1 (if num is bouncy) ) / (num_non_bouncy(num-1)+ if num is non_bouncy)


def num_bouncy(num):
    count = 0
    for n in range(0, num+1):
        if is_bouncy(n) == True:
            count += 1
            print("count is")
            print(count)
            print("n is")
            print(n)
    return count

def num_non_bouncy(num):
    count = 0
    for n in range(num+1):
        if is_bouncy(n) != True:
            count += 1
    return count


def ratio(num):
    print(num_bouncy(num))
    print(num_non_bouncy(num))
    print(num)
    print(num_bouncy(num) / num_non_bouncy(num))
    return num_bouncy(num) / num_non_bouncy(num)

def bouncy_ratio(percent):
    if percent < 0.5:
        for num in range(100, 538):
            if ratio(num) == percent:
                return num
    if 0.5 <= percent <= 0.9:
        for num in range(538, 21780):
            if ratio(num) == percent:
                return num
    else:
        num = 21780
        while True:
            if ratio(num) == percent:
                return num
            num += 1


print(bouncy_ratio(0.5))

print(is_bouncy(155349))


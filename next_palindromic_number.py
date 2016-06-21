'''
next_pal(11) == 22

next_pal(188) == 191

next_pal(191) == 202

next_pal(2541) == 2552
'''
def next_pal(val):
    # your code here
    while True:
        val += 1
        if str(val)[::-1] == str(val):
            return val


print(next_pal(11))
'''
Implement a function that successfully adds two numbers together and returns
their solution in binary. The conversion can be done before, or after the
addition of the two. The binary number returned should be a string!
Test.assert_equals(add_binary(51,12),"111111")
'''

#the art of thinking simpler is POWER

def add_binary(a,b):
    #your code here
    #binary_sum = bin(a + b)
    #b_index = binary_sum.index('b')
    #return binary_sum[b_index+1:]
    return bin(a + b)[2:]

print(add_binary(51, 12))


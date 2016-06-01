class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        num1 = bin(int(A, 2))
        num2 = bin(int(B, 2))
        bin_str = bin(int(num1, 2)+int(num2, 2))
        b_index = bin_str.index('b')
        return bin_str[b_index+1:]

s = Solution()
print(s.addBinary("11", "100"))
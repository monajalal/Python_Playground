class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        new_A = " ".join(A.split())
        if new_A == "":
            return 0
        str_list = new_A.split()
        return len(str_list[len(str_list)-1])

s = Solution()
print(s.lengthOfLastWord("d"))

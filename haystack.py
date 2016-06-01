class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        if needle==None:
            return -1
        if haystack==None:
            return -1
        if (haystack.lower().__contains__(needle.lower())):
            return haystack.index(needle)
        return -1

s = Solution()
print(s.strStr("bbbbbbbbab", "baba"))
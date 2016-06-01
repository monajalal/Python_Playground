class Solution:
    # @param A : string
    # @return an integer

    def clean_string(self, string):
        result = []
        str_list = string.split()
        for word in str_list:
            result.append(''.join(ch for ch in word if ch.isalnum()))
        return "".join(result).lower()

    def isPalindrome(self, A):
        cleaned = self.clean_string(A)
        if cleaned[::-1]==cleaned:
            return 1
        return 0

s = Solution()
print(s.isPalindrome("hiih"))
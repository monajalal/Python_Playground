class Solution:
    # @param A : string
    # @return a strings
    def clean_string(self, string):
        result = []
        str_list = string.split()
        for word in str_list:
            result.append(''.join(ch for ch in word if ch.isalnum()))
        return "".join(result).lower()

    def is_palindrome(self, string):
        if len(string)==1:
            return True
        if string[::-1]==string:
            return True
        return False

    def longestPalindrome(self, A):
        if len(A)==1:
            return A
        cleaned = self.clean_string(A)
        start_index = 0
        max = -1
        longest = None
        while (start_index < len(cleaned)-1):
            end_index = start_index
            while (end_index < len(cleaned)):
                end_index +=1
                if self.is_palindrome(cleaned[start_index:end_index]):
                    if len(cleaned[start_index:end_index]) > max:
                        longest = cleaned[start_index:end_index]
                        max = end_index-start_index

            start_index +=1
        return longest


s = Solution()
print(s.longestPalindrome("abbcccaaadaaakl"))
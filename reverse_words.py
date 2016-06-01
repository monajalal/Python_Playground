class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        word_list = A.split()
        reversed_word_list = word_list[::-1]
        return " ".join(reversed_word_list)

        

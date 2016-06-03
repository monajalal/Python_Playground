import pep8


class Solution:
    # @param A : list of integers
    # @return an integer

    def largestRectangleArea(self, A):
        global_max_sum = 0
        if len(A) == 0:
            return None
        for i in range(len(A)):
            count = 1
            round_max_sum = 0
            while i+count <= len(A)-1:
                sum = min(A[i:i+count+1]) * (count+1)
                count += 1
                if sum >= round_max_sum:
                    round_max_sum = sum
                if round_max_sum > global_max_sum:
                    global_max_sum = round_max_sum
        return max(global_max_sum, max(A))

s = Solution()
"""
list = []
list = [1]
list = [ 2, 82, 11, 89, 7, 21, 92, 13, 11, 94, 4, 96, 3 ]
list = [ 90, 58, 69, 70, 82, 100, 13, 57, 47, 18 ]

list =  [ 65, 19, 8, 39, 14, 21, 83, 87, 95, 11, 14,
          58, 11, 90,34, 96, 34, 62, 96, 38, 58, 57,
          12, 78, 57, 60, 7, 58,56, 49, 36, 67, 69,
          30, 74, 46, 97, 62, 47, 42, 43, 98,60, 32,
          39, 75, 69, 28, 35, 52, 89, 78, 4, 26, 65,
          21,39, 89, 87, 69, 48, 60, 6, 21, 5, 98, 52, 59 ]

#list = [51,33]
"""
list = [6, 2, 5, 4, 5, 1, 6]

print(s.largestRectangleArea(list))
checker = pep8.Checker()
checker.check_all()

from collections import OrderedDict
class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        list = []
        count = 0
        if len(A) == 1:
            return list.append((A[0], 1))
        for i in range(len(A)-1):
            if (A[i]==A[i+1]):
                count += 1
            else:
                count += 1
                list.append((A[i], count))
                count = 0
        list.append((A[len(A)-1], count+1))
        return list


s = Solution()
list_of_tuples = s.countAndSay('11')
for tuple in list_of_tuples:
    print(tuple)

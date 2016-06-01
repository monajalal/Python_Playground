#https://www.interviewbit.com/problems/compare-version-numbers/
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        version_list_A = A.split(".")
        version_list_B = B.split(".")
        if A==B:
            return 0

        if len(version_list_A) == len(version_list_B):
            count = 0
            for i in range(len(version_list_A)):
                if int(version_list_A[i]) == int(version_list_B[i]):
                    count += 1
                    continue
                elif int(version_list_A[i]) > int(version_list_B[i]):
                    return 1
                else:
                    return -1
            if count ==len(version_list_A):
                return 0
        #1.13 < 1.13.4
        #7.3 > 1.1.3
        #0.4 < 1.1.3
        if len(version_list_A) < len(version_list_B):
            if version_list_A == version_list_B[:len(version_list_A)]:
                #print(version_list_B[len(version_list_A):].count("0"))
                if version_list_B[len(version_list_A):].count("0")==len(version_list_B)-len(version_list_A):
                    return 0
                else:
                    return -1
            else:
                return self.compareVersion("".join(version_list_A), "".join(version_list_B[:len(version_list_A)]))
        # 1.4.6 > 1.4
        if len(version_list_A) > len(version_list_B):
            if version_list_A[:len(version_list_B)]==version_list_B:
                if version_list_A[len(version_list_B):].count("0")==len(version_list_A)-len(version_list_B):
                    return 0
                else:
                    return 1
            else:
                return self.compareVersion("".join(version_list_A[:len(version_list_B)]), "".join(version_list_B))



s = Solution()
print(s.compareVersion("1.12", "2.0.0"))
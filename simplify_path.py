
    # @param A : string
    # @return a strings
    #path = "/home/", => "/home"
    #path = "/a/./b/../../c/", => "/c"
import os
class Solution:


    def simplifyPath(self, A):
        stack = []
        result = ''
        path_list = A.split("/")
        for path in path_list:
            if path != '':
                stack.append(path)
        # stack :
        while len(stack) != 0:
            path = stack.pop()
            while path == "..":
                if len(stack) != 0:
                    path = stack.pop()
                else:
                    result += '/'
            if path == ".":
                continue
            else:
                result + '/'+path
        return result

    def abs_path(self, string):
        return os.path.abspath(string)



s = Solution()
print(s.simplifyPath("/a/./b/../../c/"))
print(s.abs_path("/a/./b/../../c/"))






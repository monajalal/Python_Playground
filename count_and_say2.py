class Solution:
    # @return a string
    def count(self,s):
        result = ''
        count = 0
        curr = None
        for i in s:
            if i != curr:
                if curr != None:
                    result+=str(count)+curr
                curr=i
                count=1
            else:
                count+=1
        result+=str(count)+curr
        return result
    def countAndSay(self, n):
        s='1'
        for i in range(2,n+1):
            s=self.count(s)
        return s

s = Solution()
print(s.countAndSay(6))
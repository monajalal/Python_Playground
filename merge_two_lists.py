from list_node import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if A == None:
            return B
        elif B == None:
            return A
        if A.val <  B.val:
            A.next = self.mergeTwoLists(A.next, B)
            return A
        else:
            B.next = self.mergeTwoLists(A, B.next)
            return B

s = Solution()
a1 = ListNode(1)
a2 = ListNode(5)
a3 = ListNode(9)
a1.next = a2
a2.next = a3

b1 = ListNode(2)
b2 = ListNode(3)
b3 = ListNode(10)
b1.next = b2
b2.next = b3

merged = s.mergeTwoLists(a1, b1)

tmp = merged
while tmp.next != None:
    print(tmp.val)
    tmp = tmp.next
print(tmp.val)












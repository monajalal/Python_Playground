from tree_node import TreeNode
from queue import Queue

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        list = []
        q = Queue()
        if A == None:
            return None
        list.append(A.val)
        if A.left != None:
            q.put(A.left)
        if A.right != None:
            q.put(A.right)
        while not q.empty():
            current = q.get()
            if current != None:
                list.append(current.val)
                if current.left != None:
                    q.put(current.left)
                if current.right != None:
                    q.put(current.right)
        return list

s = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)


t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7

level_order_list = s.levelOrder(t1)
for node in level_order_list:
    print(node, end=" ")






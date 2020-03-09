class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node('A')
n1 = Node('B')
n2 = Node('C')
n3 = Node('D')
n4 = Node('E')

root.right = n2
root.left = n1
n1.right = n4
n1.left = n3


def inorder(myroot):
    if myroot:
        inorder(myroot.left)
        print(myroot.data)
        inorder(myroot.right)

def postorder(myroot):
    if myroot:
        postorder(myroot.left)
        postorder(myroot.right)
        print(myroot.data)

def preorder(myroot):
    if myroot:
        print(myroot.data)
        preorder(myroot.left)
        preorder(myroot.left)

#inorder(root)

postorder(root)
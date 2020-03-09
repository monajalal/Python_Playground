class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node('1')
n1 = Node('2')
n2 = Node('3')
n3 = Node('4')
n4 = Node('5')

root.right = n2
root.left = n1
n1.right = n4
n1.left = n3

def search(root, val):
    if root:
        if root.data < val:
            return search(root.right, val)
        else:
            return search(root.left, val)

print(search(root, 3))

class Node:
    # class construction
    def __init__(self, val):
        self.val = val
        self.left = None  # left child --> no child yet
        self.right = None  # right child --> no child yet

    def insert(self, data):
        # don't allow duplicates in the tree

        if self.val == int(data):
            return False
        elif self.val > int(data):
            if self.left:
                self.left.insert(int(data))
                return True
            else:
                self.left = Node(int(data))
                return True
        else:
            if self.right:
                self.right.insert(int(data))
                return True
            else:
                self.right = Node(int(data))
                return True
        return False

    def find(self, data):
        if self.val == data:
            return True
        elif self.val < data:
            if self.right:
                return self.right.find(data)
            else:
                return False
        else:
            if self.left:
                return self.left.find(data)
            else:
                return False
        return False

    def inorder(self):
        if self:
            if self.left:
                self.inorder(self.left)
            print(str(self.data))
            if self.right:
                self.inorder(self.right)

    def postorder(self):
        if self:
            self.postorder(self.left)
            self.postorder(self.right)
            print(str(self.data))

    def preorder(self):
        if self:
            print(str(self.data))
            self.preorder(self.left)
            self.preorder(self.left)


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)

    def find(self, data):
        if self.root:
            self.root.find(data)
            return True
        else:
            return False

    def preorder(self):
        if self.root:
            self.root.preorder()

    def inorder(self):
        if self.root:
            self.root.inorder()

    def postorder(self):
        if self.root:
            self.root.postorder()


bst = Tree()
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(5)
bst.insert(6)
print(bst.insert(15))
bst.inorder()

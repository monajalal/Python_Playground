class Node:
    # class construction
    def __init__(self, val):
        self.val = val
        self.left = None  # left child --> no child yet
        self.right = None  # right child --> no child yet

    def insert(self, data):
        # don't allow duplicates in the tree
        #print("self val {} and data {} ".format(self.val, data))
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
                self.left.inorder()
            print(str(self.val))
            if self.right:
                self.right.inorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.val))

    def preorder(self):
        if self:
            print(str(self.val))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()


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
        print("preorder traversal of a BST tree")
        if self.root:
            self.root.preorder()

    def inorder(self):
        print("inorder traversal of a BST tree")
        if self.root:
            self.root.inorder()

    def postorder(self):
        print("postorder traversal of a BST tree")
        if self.root:
            self.root.postorder()


bst = Tree()
bst.insert(1)
#print(n1)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(5)
#print(bst.insert(6))
#print(bst.insert(15))

bst.inorder()
bst.postorder()
bst.preorder()


from LLNode import LLNode
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.last = None

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        node = LLNode(item)
        if self.last == None:
            self.last = node
        else:
            self.last.next = node
            self.size += 1

    def pop(self):
        self.size -= 1
        returned_data = self.last.data
        self.last = None
        return returned_data

"""

class Stack():
    def __init__(self):
        self.items = []

    def get_size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


stack = Stack()
print(stack.get_size())
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.pop())
print(stack.pop())
print(stack.get_size())
print(stack.is_empty())

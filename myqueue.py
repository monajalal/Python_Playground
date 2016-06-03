from LLNode import LLNode
class Queue:
    def __init__(self):
        self.size = 0
        self.head = None

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def insert(self, item):
        node = LLNode(item)
        self.size += 1
        if self.head == None:
            self.head = node
            return self.head

        tmp = self.head
        while (tmp.next != None):
            tmp = tmp.next

        tmp.next = node

        return self.head

    def remove(self):

        returned_data = self.head.data
        self.head= self.head.next
        self.size -= 1
        return returned_data

s = Queue()
s.insert(2)
s.insert(3)
s.insert(5)
print(s.remove())
print(s.get_size())
print(s.is_empty())

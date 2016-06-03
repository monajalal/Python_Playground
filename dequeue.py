#Double-ended queue
class Dequeue():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def get_size(self):
        return len(self.items)

    def add_front(self, item):
        return self.items.append(item)

    def add_rear(self, item):
        return self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)
"""
dequeue = Dequeue()
print(dequeue.is_empty())
dequeue.add_front("mona")
dequeue.add_rear("mina")
dequeue.add_front("daisy")
dequeue.add_rear("hello")
print(dequeue.get_size())
print(dequeue.remove_front())
print(dequeue.remove_rear())

"""
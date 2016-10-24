class mona_stack:
    def __init__(self):
        self.items = []


    def is_empty(self):
        return len(self.items) == 0


    def push(self, item):
        return self.items.append(item)


    def pop(self):
        return self.items.pop()


    def peek(self):
        return self.items[len(self.items)-1]


    def size(self):
        return len(self.items)

    def print(self):
        for item in self.items:
            print(item, end=', ')



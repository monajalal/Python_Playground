class LinkedListNode():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


    def data(self):
        return self.data


    def next_node(self):
        return self.next_node


    def set_next_node(self, next_node):
        self.next_node = next_node

    def search(self, data):
        index = 0
        while self.next_node != None and self != None:
            if self.data == data:
                return index
            else:
                self = self.next_node
                index += 1
        return -1

    def delete(self, data):
        head = self
        if self.data == data:
            head = self.next_node
        while self.next_node != None and self != None:
            if self.next_node.data == data:
                if self.next_node.next_node != None:
                    self.next_node = self.next_node.next_node
                else:
                    self.next_node = None
            else:
                self = self.next_node
        return head


    def insert(self, index, data):
        head = self
        if index == 0:
            tmp_node = LinkedListNode(data)
            tmp_node.next_node = self
            head = tmp_node
        else:
            idx = 0
            while self.next_node != None and self != None:
                if idx == index:
                    middle_node = LinkedListNode(data)
                    if self.next_node.next_node != None:
                        middle_node.next_node = self.next_node.next_node
                    else:
                         middle_node.next_node = None
                    self.next_node = middle_node
                else:
                    self = self.next_node
                    idx += 1
        return head


    def size(self):
        items = 0
        while self.next_node != None and self != None:
            items += 1
            self = self.next_node
        if self != None:
            items += 1
        return items

    def print(self):
        while self.next_node != None:
            print("%s: %s" % ("current node data is", self.data))
            self = self.next_node
        if self.next_node == None and self != None:
            print("%s: %s" % ("current node data is", self.data))


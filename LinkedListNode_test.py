from LinkedListNode import *

head = LinkedListNode(3)
node1 = LinkedListNode('cat')
node2 = LinkedListNode('dog')
node3 = LinkedListNode(4)
head.set_next_node(node1)
node1.set_next_node(node2)
node2.set_next_node(node3)

print(head.search('dog'))
head.delete(3)
head.delete(4)
head.insert(1, 'fish')

print(head.size())
head.print()

#checking if a string is palindrome using dequeue data structure
from dequeue import Dequeue

class Palindrome:
    def create_dequeu(self, string):
        dequeue= Dequeue()
        for char in string:
            dequeue.add_front(char)
        return dequeue

    def is_palindrome(self, string):
        dequeue = self.create_dequeu(string)
        the_same = True
        while not dequeue.is_empty():
            if (dequeue.remove_rear() != dequeue.remove_front()):
                the_same = False
                return the_same
        return the_same

palindrome = Palindrome()
print(palindrome.is_palindrome("hiih"))



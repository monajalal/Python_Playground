#checking if a string is palindrome using dequeue data structure
from dequeue import Dequeue

class Palindrome:
    def create_dequeue(self, string):
        dequeue= Dequeue()
        for char in string:
            if not char.isspace() and char.isalnum():
                dequeue.add_front(char)
        return dequeue

    def is_palindrome(self, string):
        dequeue = self.create_dequeue(string.lower())
        the_same = True
        while not dequeue.is_empty() and dequeue.get_size() > 1:
            if (dequeue.remove_rear() != dequeue.remove_front()):
                the_same = False
                return the_same
        return the_same

palindrome = Palindrome()
print(palindrome.is_palindrome("Taco cat"))




pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)

print("numbers: ", numbers)
print("letters: ", letters)
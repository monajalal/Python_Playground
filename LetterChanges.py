# change a-b ... z-a
def LetterChanges(str):
    modified_str = ''
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for letter in str:
            if letter.isalpha():
                letter = chr(ord(letter)+1)
                if letter in vowels:
                    letter = letter.capitalize()
                modified_str += letter
            else:
                modified_str += letter
    return modified_str
    


# keep this function call here
print(LetterChanges("hello*3"))
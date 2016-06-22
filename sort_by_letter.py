'''
Write a function that accepts two parameters, i) a string (containing a list of words)
and ii) an integer (n). The function should alphabetize the list based on the nth letter
of each word.

example:

function sortIt('bid, zag', 2) #=> 'zag, bid'
The length of all words provided in the list will be >= n. The format will be "x, x, x".
In Haskell you'll get a list of Strings instead.

Test.assert_equals(sort_it('bill, bell, ball, bull', 2),'ball, bell, bill, bull' , 'Sort by the second letter')
Test.assert_equals(sort_it('cat, dog, eel, bee', 3),'bee, dog, eel, cat' , 'Sort by the third letter')
'''
'''
def swap(i , j, list):
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp
'''
def swap(i, j , list):
    list[i], list[j] = list[j], list[i]


def sort_it(list_, n= None):
    #return sorted( list_, key=list_[n] )
    if n is None:
        return list_
    index = n-1
    word_list = list_.split(', ')
    for i in range(len(word_list) - 1):
        for j in range(i+1, len(word_list)):
            if word_list[i][index:] > word_list[j][index:]:
                swap(i,j, word_list)
    return ", ".join(word_list)

print(sort_it('bill, bell, ball, bull', 2))
print(sort_it("Arthur von Streit, Ernst von Eisenach, Ernst von Eisenach, Paul von Oberstein, Helmut Rennenkampf, Anton Ferner, Adalbert von Fahrenheit", 8))
print(sort_it('Oskar von Reuenthal, Neidhardt Muller, Karl Robert Steinmetz, Paul von Oberstein, Adalbert von Fahrenheit, Helmut Rennenkampf, Ernst von Eisenach, August Samuel Wahlen', None))

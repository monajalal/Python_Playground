from operator import itemgetter
fruit_list = [
    ('apple', 2),
    ('banana', 5),
    ('coconut', 1),
    ('durian', 3),
    ('elderberries', 4)
]

sorted_fruit = sorted(fruit_list, key=itemgetter(1))
print(sorted_fruit)

import datetime
from operator import attrgetter

date_list = [
    datetime.datetime(2015, 4, 29, 10, 15, 39),
    datetime.datetime(2006, 8, 15, 14, 59, 2),
    datetime.datetime(1981, 5, 16, 2, 10, 42),
    datetime.datetime(2012, 8, 9, 14, 59, 2),
]

sorted_dates = sorted(date_list, key=attrgetter('day'))
print(sorted_dates)

backwards = [
    'tac',
    'esuoheerT',
    'htenneK',
    [5, 4, 3, 2, 1],
]

def reverse(list):
    return list[::-1]

forwards = list(map(reverse, backwards))
print(forwards)

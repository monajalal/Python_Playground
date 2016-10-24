from collections import defaultdict

colors = (
    ("mona", "purple"),
    ("mina", "gold"),
    ("sara", "yellow"),
    ("maggie", "red"),
    ("margaret", "green"),
    ("mona", "gold"),
    ("mona", "green"),
    ("maggie", "pumpkin")
)

print(type(colors))
print(colors)

favorite_colors = defaultdict(list)

for name, color in colors:
    favorite_colors[name].append(color)

print(favorite_colors)

import json
json_favorite_colors = json.dumps(favorite_colors)
print("%s: %s" % ("json format is",json_favorite_colors))

from collections import Counter

favorites = Counter(name for name, color in colors)
print(favorites)
print(favorites.most_common(3))

print(Counter(['a', 'b', 'c', 'd', 'a', 'a']))
print(Counter(a=8, b=3, c=1))
print(Counter({'a':2, 'b':4, 'c':5}))

from urllib.request import urlopen

html = urlopen("http://attrition.org/misc/ee/protolol.txt", timeout=5)
print(html)

import urllib
urllib.request.urlretrieve("http://attrition.org/misc/ee/protolol.txt", 'jokes.txt')
joke_words = []
with open('jokes.txt', 'rb') as f:
    for line in f:
        line_word_array = line.strip().split()
        for word in line_word_array:
            joke_words.append(word)

print(Counter(joke_words).most_common(5))
for letter, count in Counter(joke_words).most_common(5):
    print("%s: %4d" % (letter, count))

walked_miles = [('Monday',1), ('Tuesday',2.3), ('Wednesday',3.5), ('Thursday',0.9)]
walked_miles_dict = defaultdict(float)
for key, value in walked_miles:
    walked_miles_dict[key] += value


print(walked_miles_dict)

miles_dict = {'Monday':1, 'Tuesday':2.3, 'Wednesday':3.5, 'Thursday':0.9}
for k, v in miles_dict.items():
    print("%s: %s" % (k, v))




import pandas as pd

df = pd.read_csv("/Users/mona/Downloads/finalized_gv_ih_master_updated.csv")

frame9_text = ''

for i in range(df.shape[0]):
    #if df.iloc[i]['Q3 Theme'] == 9:
    frame9_text += df.iloc[i]['news_title']

print(frame9_text)


import collections
import pandas as pd
from nltk.stem import PorterStemmer
ps = PorterStemmer()
import nltk
lemma = nltk.wordnet.WordNetLemmatizer()


import matplotlib.pyplot as plt
# Read input file, note the encoding is specified here
# It may be different in your text file

# Stopwords
stopwords = set(line.strip() for line in open('stopwords.txt'))
stopwords = stopwords.union(set(['mr','mrs','one','two','said']))
# Instantiate a dictionary, and for every word in the file,
# Add to the dictionary if it doesn't exist. If it does, increase the count.
wordcount = {}
# To eliminate duplicates, remember to split by punctuation, and use case demiliters.
for word in frame9_text.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if lemma.lemmatize(word) not in stopwords:
        if lemma.lemmatize(word) not in wordcount:
            #wordcount[ps.stem(word)] = 1
            wordcount[lemma.lemmatize(word)] = 1
        else:
            wordcount[lemma.lemmatize(word)] += 1
# Print most common word
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)
# Close the file

# Create a data frame of the most common words
# Draw a bar chart
lst = word_counter.most_common(n_print)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])
df.plot.bar(x='Word',y='Count')
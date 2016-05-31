from collections import Counter

def word_map(string):
    word_dict = {}
    stop_word_file=open("stopwords.txt", "r")
    stop_words =stop_word_file.read().split()
    for word in string.split():
        word = filter(str.isalnum, word).lower()
        word = word.strip()
        if word != '' and word not in stop_words:
            if word in word_dict.keys():
                word_dict[word] +=1
            else:
                word_dict[word] = 1

    return word_dict

file = open("story.txt", "r")

five_top_words = Counter(word_map(file.read())).most_common(5)
for letter, count in five_top_words:
    print '%s : %10d' %(letter, count)







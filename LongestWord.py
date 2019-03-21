def LongestWord(sen):
    words = sen.split(" ")
    word_dict = {}
    for word in words:
       if word.isalnum():
           word_dict[word] = len(word)
    return max(word_dict, key=word_dict.get)




# keep this function call here
print(LongestWord(input()))
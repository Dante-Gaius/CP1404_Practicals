import collections
WORD_DICTIONARY = {}
text = input("Enter a strings:")
word_list = text.split()
counter = collections.Counter(word_list)
WORD_DICTIONARY.update(counter)
max_length = max(len(words) for words in WORD_DICTIONARY)
print("Text: {}".format(text))
for words in WORD_DICTIONARY:
    print("{:{}} : {}".format(words, max_length, WORD_DICTIONARY[words]))

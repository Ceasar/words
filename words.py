import os
import string

WORDS = set()

NUMBERS = '1234567890'


def clean_word(word):
    for symbol in string.punctuation:
        if symbol in word:
            return
    for number in NUMBERS:
        if number in word:
            return
    return word.lower()


for _, _, filenames in os.walk('books'):
    for filename in filenames:
        with open("books/%s" % filename) as f:
            for line in f:
                words = line.split()
                for word in words:
                    cword = clean_word(word)
                    if cword:
                        WORDS.add(cword)
with open("dictionary.txt", 'w') as f:
    for word in sorted(WORDS):
        f.write(word + "\n")

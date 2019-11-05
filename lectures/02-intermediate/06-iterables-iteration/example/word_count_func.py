# A kind of functional word count example

from collections import defaultdict
from functools import reduce
from pprint import pprint as pp

words = '''
This is the real deal. It is imperfect, and has been written by people who 
were learning, and has been around for 8 years. Then it was through a major 
refactor and the original authors are still not happy with it but it’s 
good enough. Just like almost all legacy projects.
'''

def filter_chars(word):
    if word[-1] not in ('.', ','):
        return word
    return word[:-1]


def count(acc, item):
    acc[item] += 1
    return acc


split_words = map(lambda word: word.lower(), words.split())
processed_words = map(filter_chars, split_words)
words = reduce(count, processed_words, defaultdict(int))

for word in sorted(words, key=words.get, reverse=True):
    print(f'{word} = {words[word]}')

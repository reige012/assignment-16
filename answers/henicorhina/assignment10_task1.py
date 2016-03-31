# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 10
Refactored for BIOL7800 assignment 16
Oscar Johnson 28 February 2016
"""

import re


def quote_dict(text):
    """
    Takes text as a string and creates a dictionary of words
    Returns the dictionary and a list of the words from the string
    """
    text = text.lower()
    text = re.sub("['-,\n]", '', text)  # remove non-alphanumeric chars and \n
    text = re.sub('[.]', ' ', text)  # replace periods with whitespace
    # text = re.sub('  ', ' ', text)
    l = text.split()  # listify
    num = [0]*100
    dic = dict(zip(l, num))  # dictionary with words as keys
    return dic, l


def word_counter(dic, l):
    """
    Takes a list of words and a dictionary of those words
    Returns a count of words as a list, sorted by decreasing abundance
    """
    for word in l:  # iterate across all words in a list
        for key, value in dic.items():  # iterate across dictionary
            if word == key:
                dic[word] += 1  # increase dictionary counter when words match
    count_of_words = []
    for key, value in dic.items():
        # add words and values to list in form of tuples
        count_of_words.append((value, key))
    count_of_words.sort(reverse=True)  # sort words in descending abundance
    return(count_of_words)


def main():
    my_quote = """Stars burn a very light type of air that is packed very tight in the middle of the star. The tiny pieces of the air join to form a slightly heavier type of air that can't burn in the star without the middle being much hotter and tighter.

After a long time, all the very light air in the middle is used up. Then the star gets much hotter and tighter in the middle, so it can burn the slightly heavier air. It also also gets much bigger and cooler outside. But it is still so hot it will burn up any close-in worlds.

The sun is a star and will do this after a very long time. It will get so big that it will burn our world all up. This will not happen for at least ten hundred hundred hundred hundred years, so we don't have to worry about it now.

Long after that, a star like the sun will burn up all the slightly heavier air, too. Then it will become very tiny and hot and white, but will be so tiny it won't be able to keep its worlds warm. It will keep cooling off over a very very long time. The worlds that are left will be all ice.

But stars that are heavier can go on to burn heavier and heavier things, until finally they make the biggest flash we know. That is their end.
    """
    dictionary = quote_dict(my_quote)
    count = word_counter(dictionary[0], dictionary[1])
    print('ten most common words and count')
    for word in count[0:10]:
        print(word[1], word[0])

if __name__ == '__main__':
    main()

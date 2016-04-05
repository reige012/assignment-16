# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:46:56 2016

@author: Marco
"""

"""
Task 1
"""
# importing modules
import re

# Global Variable
STRING = ('''Stars burn a very light type of air that is packed very tight in the middle of the star. The tiny pieces of the air join to form a slightly heavier type of air that can't burn in the star without the middle being much hotter and tighter.

After a long time, all the very light air in the middle is used up. Then the star gets much hotter and tighter in the middle, so it can burn the slightly heavier air. It also also gets much bigger and cooler outside. But it is still so hot it will burn up any close-in worlds.

The sun is a star and will do this after a very long time. It will get so big that it will burn our world all up. This will not happen for at least ten hundred hundred hundred hundred years, so we don't have to worry about it now.

Long after that, a star like the sun will burn up all the slightly heavier air, too. Then it will become very tiny and hot and white, but will be so tiny it won't be able to keep its worlds warm. It will keep cooling off over a very very long time. The worlds that are left will be all ice.

But stars that are heavier can go on to burn heavier and heavier things, until finally they make the biggest flash we know. That is their end.''')


def string_standizer(string):
    '''
    this function takes all kinds of pontuation out of our string, including
    the apostrophe (') of words like can't, for example. The output will
    comprehend a lower case string with words separated by spaces.
    '''
    low = string.lower()
    without_pontuation = re.sub("\W", " ", low)
    one_space = re.sub("\s+", " ", without_pontuation)
    end_stripper = one_space.strip()
    return end_stripper


def word_counter(string):
    '''
    this function gets the word count of a string and put them as values in
    a dictionary. The words will be the keys
    '''
    word_list = string.split(" ")
    my_dict = {}
    for word in word_list:
        if word not in my_dict:
            my_dict[word] = 1
        else:
            my_dict[word] += 1
    return my_dict


def dict_reversor(my_dict):
    '''
    this function will create a list of lists. The first value of each list
    correspond the dictionary values while the second value of the list
    correspond to the dictionary keys. So, I am just reversing the dictionary
    in a way that I am not loosing any repeated value.
    '''
    keys = []
    values = []
    for key, value in my_dict.items():
        keys.append(key)
        values.append(value)
    result = sorted(list(zip(values, keys)))
    return result


def get_more_common_words(my_list, x_more_common):
    '''
    this function works by sorting a list from higher to lower values and
    adding X higher values to a new list
    '''
    sort_lista = sorted(my_list, reverse=True)
    common_values = []
    for value in sort_lista[0:x_more_common]:
        common_values.append(value)
    return common_values


def main(string):
    standard = string_standizer(string)
    dicionario = word_counter(standard)
    result = dict_reversor(dicionario)
    common = get_more_common_words(result, 10)
    print("The ten more common words are:\n")
    # this for loop will print each value in a new line
    for x, y in common:
        print(y + ": " + str(x))


if __name__ == '__main__':
    main(STRING)

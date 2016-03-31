# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Marco
# @Date:   2016-03-27 15:37:39
# @Last Modified by:   Marco
# @Last Modified time: 2016-03-31 08:12:59


def unique_fields_count(text, column=0):
    '''
    this function counts the number of unique fields in a column
    '''
    l = []
    list(map(lambda x: l.append(x[column]), text[1:]))
    my_set = set(l)
    return len(my_set)


def text2dict(text, key_column=0, value_column=1):
    '''
    gets two columns from a list of lists and create a dictionary
    '''
    my_dict = {}
    for line in text:
        if line[key_column] not in my_dict:
            my_dict[line[key_column]] = [line[value_column]]
        else:
            my_dict[line[key_column]].append(line[value_column])
    return (my_dict)


def clean_dict(my_dict):
    """remove duplicates from values"""
    new_dict = {}
    for key, values in my_dict.items():
        if key != '-999':
            new_dict[key] = set(values)
    return (new_dict)


def taxon_by_group(my_dict):
    """count how many entry each taxonomic group has"""
    for key, value in my_dict.items():
        my_dict[key] = len(value)
    return my_dict


def percent(my_dict):
    """get the percentage of each dictionary key"""
    total = 0
    new_dict = {}
    for key, values in my_dict.items():
        total += values
    for n_key, n_values in my_dict.items():
        new_dict[n_key] = str((n_values*100)/total)[:6]+'%'
    return new_dict


def main():
    with open('Supplemental_Table_6_Aves_Synonyms.txt', 'r') as fil:
        text = [line.strip('\n').split('\t') for line in fil]
    new_l = unique_fields_count(text, column=0)
    my_dict = text2dict(text, key_column=1, value_column=2)
    my_set = clean_dict(my_dict)
    values = taxon_by_group(my_set)
    perc = percent(values)
    print(new_l, '\n', my_dict, '\n', my_set, '\n', values, '\n', perc)

if __name__ == '__main__':
    main()

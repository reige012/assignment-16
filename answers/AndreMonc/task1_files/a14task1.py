# !/usr/bin/env python
# encoding: utf-8


"""
My word-counting program
Created by Andre Moncrieff on 14 March 2016, edited 21 March 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""


import argparse
from collections import Counter
import os
import glob


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir_path", required=True,
                        help="Enter the directory path of files of interest" +
                        " (assignment 14 task1-files).",
                        type=str)
    args = parser.parse_args()
    return args


class WordCounter:
    def __init__(self, dir_path):
        # set things up
        self.dir_path = dir_path
        self.list_of_filenames = self.list_of_filenames(dir_path)
        self.file_object_1 = open(self.list_of_filenames[0], "r")
        self.file_object_2 = open(self.list_of_filenames[1], "r")

        # file 1 stuff
        self.word_list_1 = self.cleaned_up_word_list(self.file_object_1)
        self.word_set_1 = self.set_of_list(self.word_list_1)
        self.total_word_count_1 = self.word_count(self.word_list_1)
        self.word_count_dict = self.count_and_dictionate(self.word_list_1)
        self.unique_word_count_1 = len(self.word_set_1)

        # file 2 stuff
        self.word_list_2 = self.cleaned_up_word_list(self.file_object_2)
        self.word_set_2 = self.set_of_list(self.word_list_2)
        self.total_word_count_2 = self.word_count(self.word_list_2)
        self.word_count_dict = self.count_and_dictionate(self.word_list_2)
        self.unique_word_count_2 = len(self.word_set_2)

        # set stuff
        self.shared = self.intersection(self.word_set_1, self.word_set_2)
        self.in_1_not_2 = self.in_1_not_2(self.word_set_1, self.word_set_2)
        self.in_2_not_1 = self.in_2_not_1(self.word_set_1, self.word_set_2)

    def list_of_filenames(self, directory_path):
        os.chdir(directory_path)
        list_of_filenames = glob.glob("*.txt")
        return list_of_filenames

    def cleaned_up_word_list(self, file_object):
        word_list = []
        punctuation = set("(),.?/!;:'\n\t@#$%^&*~+=}{[]|")
        for line in file_object:
            if line != "\n":
                cleaned_line_0 = "".join(c for c in line if c not in
                                         punctuation)
                cleaned_line_1 = cleaned_line_0.casefold()
                cleaned_line_2 = cleaned_line_1.replace("  ", " ")
                parsed = cleaned_line_2.split(" ")
                word_list.extend(parsed)
        return word_list

    def word_count(self, word_list):
        total_word_count = len(word_list)
        return total_word_count

    def set_of_list(self, some_list):
        the_set = set(some_list)
        return the_set

    def count_and_dictionate(self, some_list):
        word_count_dict = Counter(some_list)
        return word_count_dict

    def intersection(self, set1, set2):
        return len(set1.intersection(set2))

    def in_1_not_2(self, set1, set2):
        return len(set1.difference(set2))

    def in_2_not_1(self, set1, set2):
        return len(set2.difference(set1))

    def close_files(self):
        self.file_object_1.close()
        self.file_object_2.close()

def main():
    args = parser()
    word_master = WordCounter(args.dir_path)
    # print("List of Chapter 1 words: ", word_master.word_list_1)
    # print("List of Chapter 2 words: ", word_master.word_list_2)
    # print(word_master.word_set_1)
    # print(word_master.word_set_2)
    # print(word_master.cleaned_up_word_list(word_master.file_object_1))
    print("\n")
    print("The count of all words in Chapter 1: ",
          word_master.total_word_count_1)
    print("The count of unique words in Chapter 1: ",
          word_master.unique_word_count_1)
    print("The count of all words in Chapter 2: ",
          word_master.total_word_count_2)
    print("The count of unique words in Chapter 2: ",
          word_master.unique_word_count_2)
    print("The count of words in Chapter 1 that ARE in Chapter 2: ",
          word_master.shared)
    print("The count of words in Chapter 1 that ARE NOT in Chapter 2: ",
          word_master.in_1_not_2)
    print("The count of words in Chapter 2 that ARE NOT in Chapter 1: ",
          word_master.in_2_not_1)
    print("\n")
    word_master.close_files()

if __name__ == '__main__':
    main()

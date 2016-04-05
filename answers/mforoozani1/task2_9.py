#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task2 to split them by line ending
replaces the tab separations with commas, and prints out
the result - line-by-line
"""


string = """ExaML_info.T6\tLikelihood of best tree:\t-82924194.67\n
ExaML_info.T5\tLikelihood of best tree:\t-82924194.71\n
ExaML_info.T9\tLikelihood of best tree:\t-82924194.73\n
ExaML_info.T7\tLikelihood of best tree:\t-82924252.98\n
ExaML_info.T2\tLikelihood of best tree:\t-82924253.01\n
ExaML_info.T1\tLikelihood of best tree:\t-82924354.95\n
ExaML_info.T8\tLikelihood of best tree:\t-82924354.98\n
ExaML_info.T15\tLikelihood of best tree:\t-82924366.58\n
ExaML_info.T0\tLikelihood of best tree:\t-82924366.59\n
ExaML_info.T4\tLikelihood of best tree:\t-82924397.48\n
ExaML_info.T16\tLikelihood of best tree:\t-82924424.87\n
ExaML_info.T3\tLikelihood of best tree:\t-82924424.89\n
ExaML_info.T14\tLikelihood of best tree:\t-82924426.52\n
ExaML_info.T12\tLikelihood of best tree:\t-82924426.53\n
ExaML_info.T13\tLikelihood of best tree:\t-82924426.54\n
ExaML_info.T19\tLikelihood of best tree:\t-82924465.57\n
ExaML_info.T17\tLikelihood of best tree:\t-82924707.69\n
ExaML_info.T10\tLikelihood of best tree:\t-82925366.65\n
ExaML_info.T18\tLikelihood of best tree:\t-82925393.89\n
ExaML_info.T11\tLikelihood of best tree:\t-82925447.6\n """


def replace(string):
    """
    split the string by line ending,replaces the tab separations with commas
    remove the ,'', between two items in the list
    """
    string1 = string.replace("\t", ",")
    return string1


def split(string):
    string2 = string.split("\n")
    return string2


def remove(string):
    string3 = string[::2]
    return string3


def main():
    result1 = replace(string)
    print(result1)
    result2 = split(result1)
    print(result2)
    result3 = remove(result2)
    print(result3)
    for i in result3:
        print(i)

if __name__ == '__main__':
    main()

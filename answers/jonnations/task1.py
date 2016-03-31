#!/usr/bin/env python
# utf-8

"""
Modified Version of Assignment 10, Task 3
by Jon Nations on 29 March 2016
Original version on 29 February 2016
NOTE: When tesing my Assignment 10 Task 3, I realized I had an entire
function in the program that was completely unnecessary. It was
dropped, and the print function went into the if_main.
"""

from collections import OrderedDict
import operator


def code_dic(trees):
    code = trees.replace('\tLikelihood of best tree:\t', ':').replace('\n',                          ' ').split(" ")
    my_dict = OrderedDict(el.split(':') for el in code)
    # code from http://stackoverflow.com/questions/13015304/python-parse-list-of-keyvalue-elements-to-dictionary-of-key-value-pairs?lq=1
    return my_dict


def best(tree_dict):
    best_tree = sorted(tree_dict.items(), key=operator.itemgetter(1),
                       reverse=True)[-1:]
    return best_tree


def main():
    trees = """ExaML_info.T6\tLikelihood of best tree:\t-82924194.67
ExaML_info.T5\tLikelihood of best tree:\t-82924194.71
ExaML_info.T9\tLikelihood of best tree:\t-82924194.73
ExaML_info.T7\tLikelihood of best tree:\t-82924252.98
ExaML_info.T2\tLikelihood of best tree:\t-82924253.01
ExaML_info.T1\tLikelihood of best tree:\t-82924354.95
ExaML_info.T8\tLikelihood of best tree:\t-82924354.98
ExaML_info.T15\tLikelihood of best tree:\t-82924366.58
ExaML_info.T0\tLikelihood of best tree:\t-82924366.59
ExaML_info.T4\tLikelihood of best tree:\t-82924397.48
ExaML_info.T16\tLikelihood of best tree:\t-82924424.87
ExaML_info.T3\tLikelihood of best tree:\t-82924424.89
ExaML_info.T14\tLikelihood of best tree:\t-82924426.52
ExaML_info.T12\tLikelihood of best tree:\t-82924426.53
ExaML_info.T13\tLikelihood of best tree:\t-82924426.54
ExaML_info.T19\tLikelihood of best tree:\t-82924465.57
ExaML_info.T17\tLikelihood of best tree:\t-82924707.69
ExaML_info.T10\tLikelihood of best tree:\t-82925366.65
ExaML_info.T18\tLikelihood of best tree:\t-82925393.89
ExaML_info.T11\tLikelihood of best tree:\t-82925447.6"""
    tree_dict = code_dic(trees)
    for keys, values in tree_dict.items():
        print(keys,"        ", values)
    print("the best run is", best(tree_dict))


if __name__ == '__main__':
    main()

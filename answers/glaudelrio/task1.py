#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:28:07 2016

@author: Glaucia
"""

"""
Task 2

Here are some data from ExaML - a phylogenetic inference program - 
represented as a string. In this case, these data are from different runs of the program, 
and they indicate the log-likelihood scores for a set of trees inferred by the program. 
The data are tabular in format, more specifically, they are tab-delimited:


ExaML_info.T6\tLikelihood of best tree:\t-82924194.67\n
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
ExaML_info.T11\tLikelihood of best tree:\t-82925447.6\n

Write a program that processess these data to split them by line ending, 
replaces the tab separations with commas, and prints out the result - line-by-line. 
As always, your program should contain a main loop and an ifmain statement.

"""

def dealwithExaML(mydata):
    """processess ExaML data to split them by line ending, 
    replaces the tab separations with commas, and prints out the result - line-by-line."""
    #replaces the tabs by commas in the string
    mydatacommas = mydata.replace("\t", ",")
    #splits the itens in the string separated by double new lines in a list
    mydatasplitline = mydatacommas.split("\n\n")
    #iterates the itens in a lits
    for item in mydatasplitline:
        #prints each item separately
        print(item)


def main():
   dealwithExaML(mydata="""
ExaML_info.T6\tLikelihood of best tree:\t-82924194.67\n
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
ExaML_info.T11\tLikelihood of best tree:\t-82925447.6\n""")


if __name__ == "__main__":
    main()

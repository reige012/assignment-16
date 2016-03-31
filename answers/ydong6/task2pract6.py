#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Mar 22, 2016
Task 2

Write a program that does something you need (or want) for it to do. The program
can do anything, but it should have between 5 and 10 functions (or more, if you
really want). You should also write a separate set of unit tests for your
program to test that each function is performing as you would expect. You may
use any sort of input data you like (your own, someone elses, etc.). If you want
some data you could do stuff with, there are many sources online... one of my
recent favorites is this set of natural history traits of different organisms.

Be sure to trim your input data file to a reasonable size before committing it
to your repository (git does not like to store large, unchanging, files). Please
also include, in a README.md file in your repository, a description of what your
program does and how to use it. @author: York
'''
import argparse


def parser_file_input():
    """Function takes a file as input and ask for a name for output file"""
    parser = argparse.ArgumentParser(
            description="""Input a file to use and an output file name"""
            )
    parser.add_argument(
                '--input',
                required=True,
                type=str,
                help='Enter the name of the file containing text.'
            )
    return parser.parse_args()


def clean(quo):
    clean=quo.lower()
    return clean


def cleanup(quote):  
    cleaned_quote_0 = quote.replace(".", "").replace(",", "").replace(";","").replace("'","").replace(")","").replace("(","").replace(":","").replace("!","")
    cleaned_quote_1 = cleaned_quote_0.replace("\n\n", " ")
    cleaned_quote_2 = cleaned_quote_1.replace("\n","").replace(" ","")
    return cleaned_quote_2

def comb(cleaned_quote):
    a=' '.join([cleaned_quote[i:i+1] for i in range(0, len(cleaned_quote),1)])
    return a  


def makelist(parsed_quote):
           
    parsed1 = str(parsed_quote.split())
    parsed= list(parsed1)
    return parsed


def make_dict(quote_as_list):
    word_count = []
    for word in quote_as_list:
        total = 0
        for item in quote_as_list:
            if word == item:
                total += 1
        word_count.append(total)
    zip_dict = dict(zip(quote_as_list, word_count))
    print(zip_dict)
    return zip_dict


def times(mystring):
    return mystring.count('c')

def find(mystring): 
    d=mystring.find('t')
    return d
        
def replace(mystring):
    e=mystring.replace('n',"a")       
    return e 
    

def main():
    args = parser_file_input()
    with open(args.input, 'r') as thats_the_file:
        quo=thats_the_file.read()
    
    quote=clean(quo)  


    cleaned_quote = cleanup(quote)
    #print(cleaned_quote)
    a=comb(cleaned_quote)
    print(a)
    make_dict(cleaned_quote)
    
    c=times(a)
    print("Times=",c)
    d=find(a)
    print("first T position=No.",d)
    e=replace(a)
    print("replace all n=",e)
    
if __name__ == '__main__':
    main()

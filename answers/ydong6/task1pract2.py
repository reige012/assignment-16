#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Mar 22, 2016
This is the assignment 9 task1
Here is a quote from Albert Einstein:
"The most beautiful thing we can experience is the mysterious. It is the source of all true art and science."
This quote is also a string. Write a program that includes 5 different functions
each of which demonstrates one of 5 different string methods. As always, your
program should contain a main loop and an ifmain statement. 
@author: Yuankai Dong
'''

mystring = "The most beautiful thing we can experience is the mysterious. It is the source of all true art and science."


def upper(mystring):
    new_string = mystring.upper()
    return new_string
        
        
def split(mystring): 
    return mystring.split(" ")
    
        
        
def times(mystring):
        #how many times
    return mystring.count('is')
    
        
    
def find(mystring):
        
    d=mystring.find('we')
    return d
    
        
        
def lower(mystring):
    return mystring.lower()
    
        
  

def main(mystring, replaced, replacer):
    a=upper(mystring)
    print("Upper=",a)
    b=split(mystring)
    print("Split=",b)
    c=times(mystring)
    print("Times=",c)
    d=find(mystring)
    print("find=",d)
    e=lower(mystring)
    print("lower=",e)
    
   
        
    
if __name__ == '__main__':
    main(mystring, '.','!')
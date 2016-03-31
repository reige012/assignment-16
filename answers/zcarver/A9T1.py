#! /usr/bin/env python
# encoding UTF-8

'''
Assignment9Task1 biol7800
ZacCarver 02/25/2016
"The most beautiful thing we can experience is the mysterious. It is the source
of all true art and science."
Task1-Write a program that includes 5 different functions each of which
demonstrates one of 5 different string methods.
'''


def aestr1(s):
    w = s.center(30, '~')
    return w


def aestr2(s):
    aeel = s.strip().split()
    for i in aeel:
        return i


def aestr3(s):
    f = s.find("a")
    return f


def aestr4(s):
    count = 0
    for letter in s:
        if letter == 'a':
            count += 1
    return count


def AEstr5(s):
    AE = s.upper()
    rep = AE.replace(".", "!")
    return rep


def main():
    q = "The most beautiful thing we can experience is the mysterious. It is \
    the source of all true art and science."
    print("1:returns string centered of width 30 filling with ~", aestr1(q))
    print("2:returns string as a string array w/o leading \
    and trailing chars", aestr2(q))
    print("3:finds instances of 'a', .find()", aestr3(q))
    print("4:counts the instances of 'a'", aestr4(q))
    print("5:changes case of all letters and replaces '.' w/ '!'", AEstr5(q))

if __name__ == '__main__':
    main()

# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 09:08:08 2016

@author: Glaucia
"""


def reading_csv_files(file):
    new_file = []
    with open(file, 'r') as f:
        for line in f:
            new_file.append(line.strip('\n').split(','))
    return new_file


def c2v2(concentration_desired, final_volume):
    c2v2 = concentration_desired * final_volume
    return c2v2


def concentration_in_list(data_frame, col):
    concentration_list = []
    for value in data_frame:
        try:
            concentration_list.append(float(value[col]))
        except:
            pass
    return concentration_list


def DNA_volume(concentration_list, c2v2):
    DNA_amount = []
    for value in concentration_list:
        division = c2v2 / value
        DNA_amount.append(division)
    return DNA_amount


def buffer_volume(DNA_volume, final_volume):
    buffer_amount = []
    for value in DNA_volume:
        buffer = final_volume - value
        buffer_amount.append(buffer)
    return buffer_amount


def main():
    data_frame = reading_csv_files("Rheg.csv")
    print(data_frame)
    print("""The c2v2 calculation for a 10ng/uL concentration and 40uL
          as final volume:""")
    dilution = c2v2(10, 40)
    print(dilution)
    print("A list with the concentration of dsDNA in each sample:")
    concentration = concentration_in_list(data_frame, 2)
    print(concentration)
    DNA_to_add = DNA_volume(concentration, dilution)
    print("""A list with the amount of DNA to add to perform DNA dilution for
           each sample in the data_frame:""")
    print(DNA_to_add)
    buffer_to_add = buffer_volume(DNA_to_add, 40)
    print("""A list with with the amount of buffer to add to perform a DNA
           dilution:""")
    print(buffer_to_add)


if __name__ == '__main__':
    main()

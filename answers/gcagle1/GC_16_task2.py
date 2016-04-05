#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
29 March 2016
Assignment 16 Task 2

A program I wrote because my advisor ask me to re-group these 90 samples
based on year and treatment. The formatting has to be a specific way for a
program that we use. The samples are grouped in 'data_file' only by treatment.
The program uses regular expressions to separate out the different years,
writes a nested dictionary of year, treatment and sample, pretty-prints, and
writes the output to files with the first key of the dictionary (year) as the
file name.
'''

#! /usr/bin/env python
# encoding: utf-8

import re
import csv
import itertools
# import json

data_file = '''
Jp:	b1_Jp_Nov14,	b1_Jp_May15,	b1_Jp_Jun14,	b2_Jp_Nov14,	b2_Jp_May15,	b2_Jp_Jun14,	b3_Jp_Nov14,	b3_Jp_May15,	b3_Jp_Jun14,	b4_Jp_Nov14,	b4_Jp_May15,	b4_Jp_Jun14,	b5_Jp_Nov14,	b5_Jp_May15,	b5_Jp_Jun14
Jm:	b1_Jm_Nov14,	b1_Jm_May15,	b1_Jm_Jun14,	b2_Jm_Nov14,	b2_Jm_May15,	b2_Jm_Jun14,	b3_Jm_Nov14,	b3_Jm_May15,	b3_Jm_Jun14,	b4_Jm_Nov14,	b4_Jm_May15,	b4_Jm_Jun14,	b5_Jm_Nov14,	b5_Jm_May15,	b5_Jm_Jun14
Np:	b1_Np_Nov14,	b1_Np_May15,	b1_Np_Jun14,	b2_Np_Nov14,	b2_Np_May15,	b2_Np_Jun14,	b3_Np_Nov14,	b3_Np_May15,	b3_Np_Jun14,	b4_Np_Nov14,	b4_Np_May15,	b4_Np_Jun14,	b5_Np_Nov14,	b5_Np_May15,	b5_Np_Jun14
Nm:	b1_Nm_Nov14,	b1_Nm_May15,	b1_Nm_Jun14,	b2_Nm_Nov14,	b2_Nm_May15,	b2_Nm_Jun14,	b3_Nm_Nov14,	b3_Nm_May15,	b3_Nm_Jun14,	b4_Nm_Nov14,	b4_Nm_May15,	b4_Nm_Jun14,	b5_Nm_Nov14,	b5_Nm_May15,	b5_Nm_Jun14
Sp:	b1_Sp_Nov14,	b1_Sp_May15,	b1_Sp_Jun14,	b2_Sp_Nov14,	b2_Sp_May15,	b2_Sp_Jun14,	b3_Sp_Nov14,	b3_Sp_May15,	b3_Sp_Jun14,	b4_Sp_Nov14,	b4_Sp_May15,	b4_Sp_Jun14,	b5_Sp_Nov14,	b5_Sp_May15,	b5_Sp_Jun14
Sm:	b1_Sm_Nov14,	b1_Sm_May15,	b1_Sm_Jun14,	b2_Sm_Nov14,	b2_Sm_May15,	b2_Sm_Jun14,	b3_Sm_Nov14,	b3_Sm_May15,	b3_Sm_Jun14,	b4_Sm_Nov14,	b4_Sm_May15,	b4_Sm_Jun14,	b5_Sm_Nov14,	b5_Sm_May15,	b5_Sm_Jun14
'''


def keep_Nov14(s=data_file):
    '''returns a dictionary of samples from Nov 14'''
    Nov_14 = re.findall('\w*Nov\w*', data_file)
    compiled = ','.join(Nov_14)
    jp = re.findall('\w*Jp_\w*', compiled)
    jm = re.findall('\w*Jm_\w*', compiled)
    np = re.findall('\w*Np_\w*', compiled)
    nm = re.findall('\w*Nm_\w*', compiled)
    sp = re.findall('\w*Sp_\w*', compiled)
    sm = re.findall('\w*Sm_\w*', compiled)
    Nov_14_all = {'jp': jp, 'jm': jm, 'np': np, 'nm': nm, 'sp': sp, 'sm': sm}
    return Nov_14_all


def keep_May15(s=data_file):
    '''returns a dictionary of samples from May 15'''
    May_15 = re.findall('\w*May\w*', data_file)
    compiled = ','.join(May_15)
    jp = re.findall('\w*Jp_\w*', compiled)
    jm = re.findall('\w*Jm_\w*', compiled)
    np = re.findall('\w*Np_\w*', compiled)
    nm = re.findall('\w*Nm_\w*', compiled)
    sp = re.findall('\w*Sp_\w*', compiled)
    sm = re.findall('\w*Sm_\w*', compiled)
    May_15_all = {'jp': jp, 'jm': jm, 'np': np, 'nm': nm, 'sp': sp, 'sm': sm}
    return May_15_all


def keep_June14(s=data_file):
    '''returns a dictionary of samples from June 14'''
    June_14 = re.findall('\w*Jun\w*', data_file)
    compiled = ','.join(June_14)
    jp = re.findall('\w*Jp_\w*', compiled)
    jm = re.findall('\w*Jm_\w*', compiled)
    np = re.findall('\w*Np_\w*', compiled)
    nm = re.findall('\w*Nm_\w*', compiled)
    sp = re.findall('\w*Sp_\w*', compiled)
    sm = re.findall('\w*Sm_\w*', compiled)
    June_14_all = {'jp': jp, 'jm': jm, 'np': np, 'nm': nm, 'sp': sp, 'sm': sm}
    return June_14_all
    # June_14_all_joined = '\t'.join(June_14_all)
    # return June_14_all_joined


def dict_by_year(*args):
    '''writes a nested dictionary with "Nov 14", "May 15", "June 14" as the first keys'''
    names = ("Nov 14", "May 15", "June 14")
    combo = zip(names, args)
    dcombo = dict(combo)
    return dcombo


def formatted_print(dcombo):
    '''prints the values in a way I need them'''
    for key, values in dcombo.items():
        for k, v in values.items():
            print(k, ':', '\t'.join(map(str, v)))


def formatted_print_csv(dcombo):
    '''writes the first level key as the file name, and the values to the file '''
    for key, values in dcombo.items():
        filename = key + ".txt"
        with open(filename, 'w', newline='') as csvfile:
            for k, v in values.items():
                csvfile.writelines('{}:\t{},\t{},\t{},\t{},\t{}\n'.format(k, *v))


def main():
    n = keep_Nov14()
    m = keep_May15()
    j = keep_June14()
    dcombo = dict_by_year(n, m, j)
    formatted_print_csv(dcombo)

if __name__ == '__main__':
    main()

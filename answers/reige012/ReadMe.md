# Information for Reigeltask2_16.py File

**Program Purpose**

This program will take microsatellite data from a text file as input. the
program then works through various functions to separate the alleles into text
files for each populations and also determines the number of unique alleles
across all loci in each population.  This "set" of only unique alleles is
printed into a separate output file for each population and the count of
unique alleles is printed to the screen along with the set.

The original file should be input on the command line with flag --filepath
followed by the full path to the input file.
Example:
    $python reigeltask2_16.py --filepath fullpathtofile

***Input File Format***
The input file should be formatted such that instead of each individual carrying
its own unique ID they are identified by their population label. Each sample and
its corresponding alleles are on separate lines.  Each population label should
be followed by a "," and alleles should be separated by tabs. Loci with no data
should be entered as "000".

Example of Input Data Format:
NB1 ,	 235	243	 265	273	 222	226	 000	000	 569
NB1 ,	 243	243	 205	245	 222	226	 214	238	 000
NB2,     249	241	 215	247	 122	220	 214	245	 152

***Output File***
There will be an output file of all the alleles across all loci for each
population labeled in the input file. Based on above example those output files
would be listed as :
* NB1_output
* NB2_output

Additionally, there will be an output file that contains only the unique allele
values found in each population. These would be labeled as such:
* NB1_set_output
* NB2_set_output

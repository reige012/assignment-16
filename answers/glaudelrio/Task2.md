## Task2

This program shows a very simple calculation of DNA and buffer volume to do DNA dilutions in the lab. This program could be improved to allow users to add their csv files and change final volume and final concentration desired.

* **reading_csv_file**
This function reads a csv file. In this case it opens and existing file saved in the same directory as the code. Potentially, we could use argparse to deal with any csv as input file.

* **c2v2**
Calculates the left side of a concentration/volume formula, dealing with a desired DNA concentration and a desired final volume for your working DNA solution. It takes concentration and final volume as arguments. Potentially, we could use argparse, so the user can give different values in the comand line.

* **concentration_in_list**
This function will manipulate a list of lists to put the values stored in the desired column in a list of values, so we are able to perform calculations with those. We could also use dictionaries to keep track on the species Bnumbers, instead of dealing only with the numbers order in the list.

* **DNA_volume**
Simple calculation on the amount of DNA master stock that we need to add to our working stock. Takes concentration list as argument.

* **buffer_volume**
Simple calculation of the amount of buffer we need to add to our working stock to dilute the DNA.

## assignment 16

Program takes a .csv file from the dataset compiled by Myhrvold et al., here trimmed to 
include only birds.
[natural history traits of different organisms](http://esapubs.org/archive/ecol/E096/269/#data).
It then takes the data from this file and imports it to a pandas DataFrame for further analysis. 
Uses numpy to calculate the pearson correlation coefficient between adult mass and
egg mass in grams. Further updates will allow for user-specified calculations between
various variables.
Also returns counts of the families and species represented in the dataset. These are 
stored as sets that could be used further if needed.
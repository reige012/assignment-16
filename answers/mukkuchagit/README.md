

```python
I took ‘Amniote_Database_Aug_2015.csv’ file (from the link given by Dr. Brant) and trimmed this to give only columns of
class, genus, Species, adult body mass and longevity. And named it as ‘sub_table.csv’ file.

There are five major functional units in Task1.py file. And in order, each functions do the following:
[Outputs of functional units 1 and 2 are the index no. of the ‘sub_table.csv’ file
(while for this we have to consider zero index and the title row of the table
i.e. two index less than what is in the csv file).]

1. def get_organism_with_body_mass(column, bm): this returns the index no. of table
    (hence, corresponding class, genus and species of the organism) whose adult body mass 
    value is given as input value (in my code its 150).

2. def get_organism_with_longevity_morethan(column, long_y): this returns the index no. of table
    (hence, corresponding class, genus and species of the organism) whose longevity is more than
    the value that is given as input value (in my code its 114).

3. def find_unique_classes(column): this returns the name of total unique classes in the entire table.

4. def count_no_of_species(column): this returns the total number of species of the organisms in the entire table.

5. def count_no_of_genus(column): this returns the total number of genus of the organisms in the entire table.

6. def import_columns(filename): this function just inputs the file ‘sub_table.csv’ and creates dictionary.
    

```

#Cites_task2.py - A python program to manipulate and interact with the December 2014 Cites list of Peruvian birds 

##Introduction
The cites list of Peruvian birds is only accessible online in pdf format, so the author 
of this program (Andre Moncrieff) copied and pasted the pdf contents onto an excel 
spreadsheet, resulting in a cluttered and poorly-formatted file (hereafter "raw cites").

#####Objectives of program, corresponding to the 6 (non-main) functions it contains:
1. Pull species names from "raw cites" and store in memory in a list.
2. Write this list to a new excel file.
3. Pull species names from an excel file of Peru ornithological expedition data
and store in memory in a list.
4. Count the number of individuals per species from the expedition list, and store 
results in a dictionary (e.g. `{"Species name": [5]}`).
5. Insert cites status of each species into the dictionary 
(e.g. `{"Species name: [5, "Cites"], Species name2: [16, "No Cites"]}`). (The program 
outputs the spanish "No Cites" rather than the english "Not Cites", because this output
will be used for preparing specimen export documents in Peru.)
6. Write this dictionary to a csv file. (Column1 = species name, Column2 = number of 
individuals per species, Column3 = Cites Status.)


##Functions 

###Function 1:
*Objective:* Pull species names from "raw cites" and store in memory in a list.
*Tips:* Pass the filename of an excel file containing species names. This code should 
store (in a list) the species names found in the column that you specify.
```
def cites_list_cleaner(filename, column):
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    cleaned_cites_list = []
    for rowNum in range(1, sheet.get_highest_row() + 1):
        cell_content = str(sheet.cell(row=rowNum, column=column).value)
        if re.search("[A-Z][a-z]+ [a-z]+", cell_content): #not a super strict search
            capture = re.findall("([A-Z][a-z]+ [a-z]+)", cell_content)
            cleaned_cites_list.extend(capture)
        else:
            pass
    return cleaned_cites_list
```
#####Example of output:
```
['Accipiter bicolor', 'Accipiter collaris', 'Accipiter poliogaster', 'Accipiter 
striatus', 'Accipiter superciliosus', 'Busarellus nigricollis', 'Buteo albigula', 
'Buteo albonotatus', 'Buteo brachyurus', 'Buteo nitidus', . . . ]
```
    
###Function 2:
*Objective:* Write cites list in memory to a new excel file.
*Tips:* This code will work for any list that you wish to write to excel. Simply
change the name of the saved file as appropriate. Also, if you want to add a header,
you can change rowNum to 2, and set the value for the first row on the line above 
(e.g, `ws.cell(row=1, column=1).value = your_header`)
```
def write_cleaned_cites_to_excel(cleaned_cites_list):
    wb = openpyxl.Workbook()
    ws = wb.active
    rowNum = 1
    for species in cleaned_cites_list:
        ws.cell(row=rowNum, column=1).value = species
        rowNum += 1
    wb.save("clean_cites_list_of_Peruvian_birds.xlsx")
```
#####Example of output (written to excel file):
```
Accipiter bicolor
Accipiter collaris
Accipiter poliogaster
Accipiter striatus
Accipiter superciliosus
Busarellus nigricollis
Buteo albigula
Buteo albonotatus
Buteo brachyurus
Buteo nitidus
```

###Function 3:
*Objective:* Pull species names from an excel file of birds documented in an expedition to 
Peru and store in memory in a list.
*Tips:* Pass an excel file with species names to this function. The code is set to 
capture species names in column 1 of the excel file, but you can modify that easily in
the first line within the for loop.
```
def make_trip_list(filename):
    wb2 = openpyxl.load_workbook(filename)
    trip_list_sheet = wb2.active
    hyp_trip_list = []
    for rowNum in range(1, trip_list_sheet.get_highest_row() + 1):
            cell_content = str(trip_list_sheet.cell(row=rowNum, column=1).value)
            if re.search("[A-Z][a-z]+ [a-z]+", cell_content):
                hyp_trip_list.append(cell_content)
    return hyp_trip_list
    
```
#####Example of output:
['Contopus sordidulus', 'Anabazenops dorsalis', 'Turdus leucops', 'Colonia colonus', 
'Anabazenops dorsalis', 'Ramphocelus carbo', 'Microcerculus marginatus', 
'Poecilotriccus latirostris', 'Synallaxis cabanisi', 'Dysithamnus mentalis', . . . ]

###Function 4:
*Objective:* Count the number of individuals per species from the expedition list, and store 
results in a dictionary (e.g. `{"Species name": [5]}`). The `some_trip_list` passed to 
this function must be in the format of the output from Function 1.
```
def trip_list_counted(some_trip_list):
    species_count = []
    for species in some_trip_list:
        total = 0
        for item in some_trip_list:
            if species == item:
                total += 1
        species_count.append([total])
    zip_dict = dict(zip(some_trip_list, species_count))
    return zip_dict
```
#####Example of output: 
{'Accipiter collaris': [1], 'Synallaxis cabanisi': [4], 'Rhynchocyclus fulvipectus': [1], 
'Xiphocolaptes promeropirhynchus': [1], 'Grallaricula flavirostris': [2], 'Hydropsalis 
maculicaudus': [2], 'Muscisaxicola fluviatilis': [4], 'Cacicus solitarius': [1], 
'Myiodynastes maculatus': [4], . . . }

###Function 5:
*Objective:* Insert cites status of each species into the dictionary 
(e.g. `{"Species name: [5, "Cites"], Species name2: [16, "No Cites"]}`). The program 
outputs the spanish "No Cites" rather than the english "Not Cites", because this output
will be used for preparing specimen export documents in Peru. 
*Tips:* The `trip_num_dict` passed to this function must be in the format of the output 
from Function 4. The `cites_list` passed to this function must be in the format of the 
output from Function 1.
```
def add_cites_status_to_dict(trip_num_dict, cites_list):
    for key in trip_num_dict.keys():
        if key in cites_list:
            trip_num_dict[key].append("Cites")
        else:
            trip_num_dict[key].append("No Cites")
    return trip_num_dict
```
#####Example of output:
```
{'Anisognathus somptuosus': [4, 'No Cites'], 'Phaethornis hispidus': [2, 'Cites'], 
'Heliodoxa branickii': [1, 'Cites'], 'Cranioleuca vulpecula': [9, 'No Cites'], 
'Dixiphia pipra': [2, 'No Cites'], 'Pyrrhura roseifrons': [3, 'Cites'], 
'Satrapa icterophrys': [6, 'No Cites'], 'Emberizoides herbicola': [3, 'No Cites'], 
'Glaucidium brasilianum': [2, 'Cites'] . . . }
```

###Function 6:
*Objective:* Write output of Function 5 to a csv file. (Column1 = species name, Column2 = 
number of individuals per species, Column3 = Cites Status.) *Tips:* The `final_dict` 
passed to this function must be in the format of the output from Function 5.
```
def write_summary_to_csv(final_dict):
    writer = csv.writer(open("cites_summary.csv", 'w'))
    writer.writerow(["Species", "Number Collected", "Cites Status"])
    for key, value in final_dict.items():
        writer.writerow([key, value[0], value[1]])
```
#####Example of output (written to csv file):
```
Species,Number Collected,Cites Status
Anisognathus somptuosus,4,No Cites
Phaethornis hispidus,2,Cites
Heliodoxa branickii,1,Cites
Cranioleuca vulpecula,9,No Cites
Dixiphia pipra,2,No Cites
Pyrrhura roseifrons,3,Cites
Satrapa icterophrys,6,No Cites
Emberizoides herbicola,3,No Cites
Glaucidium brasilianum,2,Cites
Icterus cayanensis,1,No Cites
Eubucco versicolor,2,No Cites
```


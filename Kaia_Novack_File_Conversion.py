'''
┌───────────────────────────────────────────────────────────────────────────┐
│                              File Conversion                              │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: K.Novack                                                            │
│ Log:  3/4/2024 - Finished product 1.0                                     |                                      
│ Bugs: n/a                                                                 │
│ Description: Takes in a file, reads it, creates headers, makes the file a |
| csv so that it can be imported to excel.                                  │
└───────────────────────────────────────────────────────────────────────────┘
'''

import csv
column_widths = {
            "ID": 6,
            "FirstName": 15,
            "LastName": 15,
            "Grade": 6,
            "GPA": 6,
            "BirthDate": 12,
            "Gender":7,
            "ClassRank": 9,
            "AttendPct": 10,
            "Honors": 7,
            "Sports": 9,
            "ClubCount": 10
        }

columns = list(column_widths.keys())                                                                             #creates a list of the columns with their titles

def format_line(line):
    
    data = {}
    starting_positions = [0]

    for width in column_widths.values():                                                                         #for each column width using their values (lengths)
        starting_positions.append(starting_positions[-1]+width)                                                  #add to the starting positions to create the column

    for i, column  in enumerate(columns):                                                                        #for every person in the column
        data[column] = line[starting_positions[i]:starting_positions[i+1]].strip()                               #add the data
    return data
def main ():                                                                                                    
    file_name = input('Enter the file name: ')                                                                   #creates a value for the user to input a file
    formatted_data = []

    try:                                                                                                         #trys the input
        with open(file_name, 'r') as file_hand:                                                                  #creates a value to open the file
            lines = file_hand.readlines()                                                                        #reads the file
    except:                                                                                                      #if the user enters a value that is not a file
        print('File cannot be opened:', file_name)                                                               #print "The file cannot be opened: (file_name)"
        exit()   

    for line in lines[1:]:                                                                                       #for every line under the titles
        formatted_data.append(format_line(line))                                                                 #add the formatted data

    outfile = input('Enter output file name: ')

    with open(outfile, 'w', newline='') as csvfile:                                                              #writes the new file
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()                                                                                     #writes the headers
        writer.writerows(formatted_data)                                                                         #writes the rows using the formatted data
    print("Successful!")                                                                                         #lets the user know that the proccess is complete
main()
    
    


    



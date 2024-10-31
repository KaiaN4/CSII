'''
┌───────────────────────────────────────────────────────────────────────────┐
│                               Space Invaders                              │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: K.Novack                                                            │
│ Log: 10/31/2024 - Finished product 1.0                                    |                                      
│ Bugs: n/a                                                                 │
│ Description: Takes in a file, reads it, sorts it from least to greatest   |
| frequency, and then puts sorts them into words and frequency's            |
| (key, value) in an excel spreadsheet.                                     │
└───────────────────────────────────────────────────────────────────────────┘
'''

import csv                                                                                                       #import the csv library

def final_text(counts,removed_punctuation):                                                                      #creates a new function called final_text
    removed_punctuation = removed_punctuation.translate(str.maketrans('','', removed_punctuation))               #removes the punctuation in the speech
    counts_sorted = {key: val for key, val in sorted(counts.items(), key = lambda ele: ele[1], reverse = True)}  #sorts the speech from greatest frequency to least
    amounts = 20                                                                                                 #allows there to be no more than 20 words when given in excel
    counts_next = dict(list(counts_sorted.items()) [0: amounts])                                                 #counts the amount of words and makes sure there are no more than 20 words
    return(counts_next)                                                                                          #returns the list of words and their frequencies


def main ():                                                                                                     #creates a main function
    file_name = input('Enter the file name: ')                                                                   #creates a value for the user to input a file
    try:                                                                                                         #trys the input
        file_hand = open(file_name)                                                                              #creates a value to open the file
    except:                                                                                                      #if the user enters a value that is not a file
        print('File cannot be opened:', file_name)                                                               #print "The file cannot be opened: (file_name)"
        exit()                                                                                                   #exits the try loop

    counts = dict()                                                                                              #sets count to dictionary
    removed_words = ["and", "a", "for", "he", "with", "the", "am", "is", "are", "was", "were", "be", "being", "been", "has", "have", "had", "do", "does", "did", "may", "might", "must", "can", "could", "shall", "should", "will", "would", "my", "i", "we", "us", "it", "they", "all", "them", "of", "in", "out", "on", "at", "above", "no", "she", "not", "we", "so", "as", "to", "an", "that", "this", "but", "who", "by", "or", "than", "its", "what"] #creates a list of words to remove from the inputed text
    removed_punctuation = ":.;'"                                                                                 #creates a list of punctuation to removed

    for line in file_hand:                                                                                       #for every line in the file
        line = line.lower()                                                                                      #makes all of the letters lowercase
        line = line.split()                                                                                      #split the lines with a space
        for word in line:                                                                                        #for every word in words
            if word in removed_words:                                                                            #if there is a word in the text that is in removed words:
                continue                                                                                         #skip over the word
            if word not in counts:                                                                               #first, if the word is not in the dictionary
                counts[word] = 1                                                                                 #keeps the value of that word
            else:                                                                                                #if the word is in the dictionary
                counts[word] += 1                                                                                #add that word to the wordcount of the text

    counts_next = final_text(counts,removed_punctuation)                                                         #creates a variable that runs final_text with the perameters of counts and removed_punctuation
    print(counts_next)                                                                                           #prints counts_next for the user


    header_list = ['words', 'amount']                                                                            #creates a list for headers with the names words and amounts

    with open('Kaia_Novack_Election_Data_Excel2.csv','w',newline='') as csv_file:                                #create a new line to enter the words and their frequencies
        writer = csv.writer(csv_file)                                                                            #writes a csv file
        writer.writerow(header_list)                                                                             #writes the header for words and amounts
        for key, value in counts_next.items():                                                                   #for every word and its frequency:
            writer = csv.writer(csv_file)                                                                        #inserts the word and frequency into the excel file
            writer.writerow([key, value])                                                                        #write the word and frequency into its designated column

main()                                                                                                           #run the main function

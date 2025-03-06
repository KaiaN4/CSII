'''
┌───────────────────────────────────────────────────────────────────────────┐
│                            Tupple Functions                               │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: K.Novack                                                            │
│ Log:  3/4/2024 - Finished product 1.0                                     |                                      
│ Bugs: n/a                                                                 │
│ Description: Takes in a file, reads it, and performs one of three actions.│
|        1. Allows the user to check the user with the most emails          |
|        2. Allows the user to check the disdribution of hours              |
|        3. Allows the user to see the letters in decreasing order          |
└───────────────────────────────────────────────────────────────────────────┘
'''


def emails(filename):
    email_counts = {}                                                          # Dictionary to store email addresses and their counts

    with open(filename) as file:
        for line in file:
            if line.startswith("From:"):
                email = line.split()[1]                                       # Extract email address from the line
                email_counts[email] = email_counts.get(email, 0) + 1          # Increment count

  
    count_list = [(email, count) for email, count in email_counts.items()]  # Create a list of tuples (count, email)

 
    count_list.sort(reverse=True)                                         # Sort the list in reverse order based on count


    print(count_list[0])                                                      # Print the person with the most commits

def count_hours(filename):
    hcount = dict()                                     #create empty dictionary
    times = []                                           #create empty list
    with open(filename) as file:
        for line in file: 
            words = line.split()
            if len(words) > 2 and words[0] == 'From':       #Select lines with 'From'
                hr = words[5].split(':')                    #Select hour (5th index) and split string with colon
                hcount[hr[0]] = hcount.get(hr[0], 0) + 1    #increase count for each hour
            else:
                continue

        for k,v in hcount.items():                           #k = hour, v = count
            times.append((k,v))                               #append tuples to list

        times.sort()                                         #sort list by hour
        for k,v in times:                                    #loop through list of tuples
            print(k,v)                                      #print counts sorted by hour

def letter_frequency(filename):
    letter_counts = {}
    with open(filename, 'r') as file:
        text = file.read().lower()                                                              #Convert to lowercase
        for char in text:
            if char.isalpha():                                                                  #Only count letters
                letter_counts[char] = letter_counts.get(char, 0) + 1 


    sorted_letters = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)       # Sort by frequency in descending order
    
    for letter, count in sorted_letters:
        print(f"{letter}: {count}") 




def main():
    filename = input("Please enter your file name: ")
    try:                                                                                                         #trys the input
        with open(filename, 'r') as file_hand:                                                                  #creates a value to open the file
            which = input("Do you want to see the highest emails (1), distribution of hours (2), or letters in decreasing orders of frequency(3)?  ")
            if which == "1":
                emails(filename)
            elif which == "2":
                count_hours(filename)
            elif which == "3":
                letter_frequency(filename) 
    except:                                                                                                      #if the user enters a value that is not a file
        print('File cannot be opened:', filename)                                                               #print "The file cannot be opened: (file_name)"
        exit()   

main()
'''
1. Ask the user for their name
2. Create the menu
    a. Get the first name
    b. Get the middle name(s)
    c. Get the last name
    d. Determine the number of vowels in the full name
        i. Can prompt for a certain letter
    e. Return true if your last name has a hyphen
    f. Make the name lower case (cannot use .lower)
    g. Make the name upper case (cannot use .upper)
    h. Create a random name with the letters in the person's original name
    i. Return true if the name is a palindrome
    j. Return true if the name has a title/distinction
3. Take in the name to perform the tasks
4. Create functions for each task on the menu
'''

import random

def contains_title(name):
    if "." in name:
        return True
    special_titles = ["Dr.", "dr.", "Sr.", "sr.", "Jr.", "jr."]                 #creates a list for the special titles
    for n in name.split(" "):                                                   #splits the name 
        if n in special_titles:
            return True
    return False

def remove_title(name):                                                        #creates a function to remove the title for the rest of the functions
    name = name.split(" ")
    special_titles = ["Dr.", "Sr.", "Jr."]
    for n in name:                                                             #for the different names (first, middle, last)
        if n in special_titles:
            name.remove(n)         #can i use remove (list function)?          #removes the title
    return name

def get_fn(name):
    name = remove_title(name)
    return name[0]                                                             #returns the first name

def get_mn(name):
    name = remove_title(name)
    if len(name) < 3:                                                          #if the length of the name is less than 3
        return("You do not have a middle name!")                               #then the user has no middle name
    name.pop(0)                #can i use pop (list function)?                 #removes the first name
    name.pop(-1)                                                               #removes the last name
    
    result = ""

    for n in name:
        result += n
    return result                                                              #return the middle name

def get_ln(name):
    name = remove_title(name)
    if len(name) >= 2:                                                        #if the length of the name is greater than or equal to 2
        return name[-1]                                                       #return the last name
    else:
        return("There is no last name!")

def determine_vowels(name):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    
    for n in name:
        if n in vowels:                                                      #if the letter in the name is in the vowels list
            count += 1                                                       #add it to the count
    return count

def return_hyphen(name):
    if '-' in name.split(" ")[-1]:                                           #if there is a hyphen in the last name
        return True
    
def lower_case(name):
    result = ""
    for char in name:
        if 'A' <= char <= 'Z':                                              #if the letter is upper case
            result += chr(ord(char) + 32)                                   #makes the upper case letter lower case using the ascii scale and adds it to the result
        else:
            result += char                                                  #keep the character and add it to the result
    return result

def upper_case(name):
    result = ""
    for char in name:
        if 'a' <= char <= 'z':                                              #if the character is lower case
            char_code = ord(char)
            upper_char_code = char_code - 32
            result += chr(upper_char_code)                                  #add the character to the result
        else:
            result += char
    return result

def random_name(name):
    letters = list(name)
    new_name = ""

    for i in range(len(letters)):                                          #for every letter in the name
        letter = random.choice(letters)                                    #choose a random letter
        new_name += letter                                                 #add the letter to the new name
        letters.remove(letter)    #need a space?                           #remove the letter so that each letter only appears once
    return new_name

def palindrome(name):
    if name == name[::-1]:                                                 #if the original name is equal to the name backwards
        return True
    else:
        return False
    
def main():
    name = input("Welcome to the program! Please enter your full name: ")
    for i in range(len(name)):                                            #splits the name into letters
        ascii_value = ord(name[i])                                        #makes the letters in the name numbers on the ascii scale
    if (ascii_value <= 65 and ascii_value <= 90) and (ascii_value <= 97 and ascii_value <= 122) and (ascii_value == 32) or (ascii_value == 46):         #checks if what is entered is a number
        print("Yay")
    else:            
        print("Please enter characters only in the English alphabet!")

    menu = input('''
        1. Get the first name
        2. Get the middle name(s)
        3. Get the last name
        4. Determine the number of vowels in the full name
        5. Return true if your last name has a hyphen
        6. Make the name lower case (cannot use .lower)
        7. Make the name upper case (cannot use .upper)
        8. Create a random name with the letters in the person's original name
        9. Return true if the name is a palindrome
        10. Return true if the name has a title/distinction
        
        Please enter the number you would like the computer to perform: ''')
    
    if menu not in "1 2 3 4 5 6 7 8 9 10".split(" "):
        print("Please enter a number shown!")
    elif menu == "1":
        print(get_fn(name))
    elif menu == "2":
        print(get_mn(name))
    elif menu == "3":
        print(get_ln(name))
    elif menu == "4":
        print(determine_vowels(name))
    elif menu == "5":
        print(return_hyphen(name))
    elif menu == "6":
        print(lower_case(name))
    elif menu == "7":
        print(upper_case(name))
    elif menu == "8":
        print(random_name(name))
    elif menu == "9":
        print(palindrome(name))
    elif menu == "10":
        print(contains_title(name))

main()
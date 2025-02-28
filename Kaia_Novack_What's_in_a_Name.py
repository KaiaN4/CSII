'''
┌───────────────────────────────────────────────────────────────────────────┐
│                            What's in a Name                               │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: K.Novack                                                            │
│ Log: 02/11/2025 - Finished product 1.0                                    |                                      
│ Bugs: n/a                                                                 │
│ Description: Asks a user to input their name and can perform a variety of |
| different tasks. The user will see a menu, and can choose a task for the  |
| computer to complete. The menu items are completed without the use of     |
|  global variables and helper classes.                                     |
└───────────────────────────────────────────────────────────────────────────┘
'''

'''
1. Ask the user for their name
2. Create the menu
3. Take in the name to perform the tasks
4. Create functions for each task on the menu
'''

import random
import sys

def contains_title(name):
    '''
    Checks if the user's input contains a title
    Args:
        name
    Returns:
        boolean: True
    '''
    if "." in name:
        return True                                                             #returns true it there is a period in the name
    special_titles = ["Sir", "Esq"]                                             #creates a list for the special titles
    for n in name.split(" "):                                                   #splits the name 
        if n in special_titles:
            return True
    return False

def remove_title(name):                                                        #creates a function to remove the title for the rest of the functions
    '''
    If the user's name has a title, it will remove it
    Args:
        name
    Returns:
        str: the name without the title
    '''
    name = name.split(" ")
    special_titles = ["Sir", "Esq"] 
    for n in name:                                                             #for the different names (first, middle, last)
        if "." in n:                                                           #if there is a period in the name
            name.remove(n)                                                     #removes the title
        if n in special_titles:                                                
            name.remove(n)                                                     #remove any other special titles

    return name

def get_fn(name):
    '''
    Gets the first name of the user
    Args:
        name
    Returns:
        str: the first name
    '''
    name = remove_title(name)
    return name[0]                                                             #returns the first name

def get_mn(name):
    '''
    Gets the user's middle name if there is one
    Args:
        name
    Returns:
        str: the user's middle name, or tells them if they do not have one
    '''
    name = remove_title(name)
    if len(name) < 3:                                                          #if the length of the name is less than 3
        return("You do not have a middle name!")                               #then the user has no middle name
    return " ".join(name[1:-1])

    
def get_ln(name):
    '''
    Gets the user's last name
    Args:
        name
    Returns:
        str: the user's last name, or tells them if they do not have one
    '''
    name = remove_title(name)
    if len(name) >= 2:                                                        #if the length of the name is greater than or equal to 2
        return name[-1]                                                       #return the last name
    else:
        return("There is no last name!")

def determine_vowels(name):
    '''
    Determines the number of vowels in the user's name
    Args:
        name
    Returns:
        list: the count of vowels present in the name
    '''
    name = remove_title(name) 
    vowels = list("aeiou")
    counts = [0]*5

    for n in name:
        lower = lower_case(n)
        for letter in lower:
            for i in range(len(vowels)):                                                #for every letter in vowels
                if letter == vowels[i]:                                                 #if letters in vowels
                    counts[i] += 1                                                      #add it to the count
    result = ''

    for i in range(len(vowels)):
        if counts[i] > 0:                                                               #if there are consonants
            result += f'{vowels[i]}: {counts[i]}\n'
    return result


def return_hyphen(name):
    '''
    Determines if the user's last name has a hyphen
    Args:
        name
    Returns:
        boolean: True
    '''
    return '-' in name.split(" ")[-1]                                        #if there is a hyphen in the last name
    
def lower_case(name):
    '''
    Makes the user's name all lower case without the use of the .lower function
    Args:
        name
    Returns:
        str: the lower case version of the name
    '''
    result = ""
    for char in name:
        if 'A' <= char <= 'Z':                                              #if the letter is upper case
            result += chr(ord(char) + 32)                                   #makes the upper case letter lower case using the ascii scale and adds it to the result
        else:
            result += char                                                  #keep the character and add it to the result
    return result

def upper_case(name):
    '''
    Makes the user's name upper case without the use of the .upper function
    Args:
        name
    Returns:
        str: the upper case version of the name
    '''
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
    '''
    Creates a random name using the letters in the user's original name
    Args:
        name
    Returns:
        str: the randomized name
    '''
    letters = list(name)
    new_name = ""

    for i in range(len(letters)):                                          #for every letter in the name
        letter = random.choice(letters)                                    #choose a random letter
        new_name += letter                                                 #add the letter to the new name
        letters.remove(letter)                                             #remove the letter so that each letter only appears once
    return new_name

def palindrome(name):
    '''
    Determines if the user's name is a palindrome
    Args:
        name
    Returns:
        boolean: True
    '''
    name = remove_title(name)
    first_name = name[0]
    temp = reverse_name(name[0])
    if temp == first_name:                                                 #checks if the reversed name is equal to the first name
        return True
    else:
        return False

def reverse_name(name):
    '''
    Reverses the user's name
    Args:
        name
    Returns:
        str: the reversed version of the user's name
    '''
    temp2 = name[::-1]                                                      #returns the name, but reversed
    return temp2

def make_initials(name):
    '''
    Gets the initials of the user's name
    Args:
        name
    Returns:
        str: the intials
    '''
    name = remove_title(name)
    return " ".join(n[0] + "." for n in name)                               #returns the first letter of each list item in the name

def sorted_characters(name):
    '''
    Sorts the characters into alphabetical order
    Args:
        name
    Returns:
        list: the characters in order
    '''
    cleaned_name = name.replace(" ", "")                                     #replaces the space with now space
    sorted_chars = sorted(cleaned_name)                                      #sorts the characters
    return sorted_chars

def number_of_consonants(name):
    '''
    Determines the number of consonants in the user's name
    Args:
        name
    Returns:
        list: the count of each consonant present in the name
    '''
    name = remove_title(name)                   
    consonants = list("bcdfghjklmnpqrstvwxyz")
    counts = [0]*21

    for n in name:
        lower = lower_case(n) 
        for letter in lower:
            for i in range(len(consonants)):                                   #for every letter in consonants
                if letter in consonants[i]:                                    #check if the letter[i] is in consonants
                    counts[i] += 1                                             #add it to the count
    result = ''

    for i in range(len(consonants)):
        if counts[i] > 0:                                                      #if there are consonants
            result += f'{consonants[i]}: {counts[i]}\n'                        #make the result a consonant: number of the consonant
    return result

def print_ascii(name):
    '''
    Determines the ascii scale of each letter of the user's input
    Args:
        name
    Returns:
        list: the count of each letter in its ascii value
    '''
    value = []
    for i in range(len(name)):                                                     #splits the name into letters
        ascii_value = ord(name[i])                                                 #makes the letters in the name numbers on the ascii scale
        value.append(ascii_value)
    return (value)

def print_pyramid(name):
    '''
    Prints the name in a pyramid
    Args:
        name
    Returns:
        str: name in a pyramid form
    '''
    n = len(name)
    pyramid = ''
    for i in range(n):
        multiply = n - i - 1
        pyramid += "\n" + " " * multiply + ''.join(name[:i+1])                   #creates a new line, adds a space, multiplies it for the letters in the name, and join everything together
    return pyramid

def main():
    '''
    Asks the user to input their name and allows them to pick a task for the computer to complete
    Returns:
        the return of the function the user chooses
    '''
    while True:
        play_game = input("Do you want to play: ")
        game = lower_case(play_game)
        if game == "yes" or game == "y":
            print("\n")
        elif game == "no" or game == "n":
            sys.exit()
        else:
            print("Please enter yes or no!")
            continue
        name = input("Welcome to the program! Please enter your full name: ")
        bad_characters = list("1234567890!@#$%^&*()_+={}[]\|:;<>,?/~`")
        if any(char in bad_characters for char in name) or ("  ") in name or name == (" "):       #if the name does not contain just letters
            print("Please enter a name with letters only from the english alphabet!")
            continue
        else:       
            menu = input('''
            Menu:
            1. Get your first name
            2. Get your middle name(s)
            3. Get your last name
            4. Determine the number of vowels in your full name
            5. Return true if your last name has a hyphen
            6. Make your name lower case 
            7. Make your name upper case 
            8. Create a random name with the letters of your original name
            9. Return true if your first name is a palindrome
            10. Return true if your name has a title/distinction
            11. Reverse your name
            12. Get the intials of your name
            13. Print the list of letters in your name in alphabetical order
            14. Get the number of consonants in your name
            15. See your name as an ascii value
            16. See your name in the form of a pyramid
                
            Please enter the number you would like the computer to perform: ''')
                
            if menu not in "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16".split(" "):
                print("Please enter a number shown!")
            elif menu == "1":
                print(get_fn(name))
                print()
            elif menu == "2":
                print(get_mn(name))
                print()
            elif menu == "3":
                print(get_ln(name))
                print()
            elif menu == "4":
                print(determine_vowels(name))
                print()
            elif menu == "5":
                print(return_hyphen(name))
                print()
            elif menu == "6":
                print(lower_case(name))
                print()
            elif menu == "7":
                print(upper_case(name))
                print()
            elif menu == "8":
                print(random_name(name))
                print()
            elif menu == "9":
                print(palindrome(name))
                print()
            elif menu == "10":
                print(contains_title(name))
                print()
            elif menu == "11":
                print(reverse_name(name))
                print()
            elif menu == "12":
                print(make_initials(name))
                print()
            elif menu == "13":
                print(sorted_characters(name))
                print()
            elif menu == "14":
                print(number_of_consonants(name))
                print()
            elif menu == "15":
                print (print_ascii(name))
                print()
            elif menu == "16":
                print(print_pyramid(name))
                print()
            else:
                print("Please enter the number of one of the options shown!")
        continue
        
main()
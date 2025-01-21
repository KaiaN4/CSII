'''
┌───────────────────────────────────────────────────────────────────────────┐
│                                Hangman                                    │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: K.Novack                                                            │
│ Log: 01/10/2025 - Finished product 1.0                                    |                                      
│ Bugs: n/a                                                                 │
│ Description: Asks a user to play hangman. If the player says yes, the     |
| computer will randomly choose a word from a list of words. The word will  |
| then be hidden and will be printed on the screen. Then, the computer also |
| prints the hangman, and every time the user enters a wrong letter, part of|
| the hangman is added. When a player guesses an incorrect letter, the      |
| computer also lets them know that the letter is not in the word The       |
| computer also lets the user know the letters they have guessed so that    |
| they do not guess the same letter twice.                                  |
└───────────────────────────────────────────────────────────────────────────┘
'''

import random                                                                           #imports the random library
import sys                                                                              #imports the sys library

HANGMAN_PICS = ['''
-+---+
 O   |
/|\  |
/ \  |
     ===''','''
-+---+
 O   |
/|\  |
/    |
     ===''','''
-+---+
 O   |
/|\  |
     |
    ===''','''
-+---+
 O   |
/|   |
     |
     ===''','''
+---+
O   |
|   |
    |
    ===''','''
+---+
O   |
    |
    |
    ===''','''
+---+
    |
    |
    |
    ===''']                                                                       #creates the images for hangman

words = ['hello','world', 'python', 'best', 'worst', 'awesome', 'supercalifragilisticexpialidocious', 'hola', 'charger', 'cards', 'country', 'pencil', 'phone', 'sweater', 'building', 'clock', 'home', 'wonderful', 'classroom', 'window', 'panda', 'dolphin', 'monkey', 'flashlight', 'firework', 'summer', 'winter', 'spring', 'fall', 'green']   #creates a list of words
max_guesses = 6                                                                   #sets the max guesses equal to 6

while True:
    play = input("Do you want to play hangman (yes/no): ").lower()                #asks the user if they want to play hangman
    
    if play.strip() == 'yes':                                                     #if the user says yes
        pass                                                                      #do not go through the rest of the loop
    elif play.strip() == 'no':                                                    #if the user says no
        print("Have a nice day")                                                  
        sys.exit()                                                                #fully exits the game
    else:                                                                         #if the user does not say yes or no
        print("Please enter yes or no!")                                    
        continue                                                                  #restart the while true
    
    secret = random.choice(words)                                                 #the computer selects a random word
    secret_list = list(secret)                                                    #makes a list out of the secret word
    hidden = []                                                                   #creates a list for the hidden word
    guessed_letters = []                                                          #creates a list for incorrect guesses
    guesses = 6                                                                   #sets the guesses equal to 0

    for character in secret_list:                                                 #for every letter in the word
        if character == ' ':                                                      #if there is a character
            hidden.append(' ')                                                    #add a space inbetween
        else:
            hidden.append('_')                                                    #make the characters underscores

    print(''.join(hidden))                                                        #print the hidden list
    print(HANGMAN_PICS[max_guesses])                                              #print the hangman

    while guesses > 0:                                                            #while the number of guesses is greater than 0
        if '_' not in hidden:                                                     #if there is no underscore in the hidden list
            print ("You won!")                                              
            print("The word was:",secret)                                         #print the word
            break                                                           
                                                       
        guess = input('Enter a letter: ').lower()                                 #asks the user to input a letter

        if guess.strip() not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:            #if the guess is not an alphabetical letter
            print('Enter a letter please!')                                  
        elif guess in guessed_letters:                                            #if the guessed letter has already been guessed
            print("Please enter a letter you have not already guessed")        
        elif guess in secret_list:                                                #if the guess is in the word
            for index in range(len(secret_list)):                                 #for the index in the length of the word
                if guess == secret_list[index]:                                   #if the guess matches an index
                    hidden[index] = guess                                         #make that index the guessed letter
            guessed_letters.append(guess)                                         #adds the letter to the guessed list
        else:                                                                     #if the guess is not in the word
            print('\nLetter not here!')                                         
            guesses -= 1                                                          #subtract one to the amount of guesses
            guessed_letters.append(guess)                                         #add the letter to the guessed letters
        print("Guessed letters: ", (','.join(guessed_letters)))                   #print the guessed letters 
        print(''.join(hidden))                                                    #print the word guessed so far
        print(HANGMAN_PICS[guesses])                                              #print the hangman
        print("You have", guesses, "lives left")

    if guesses == 0:                                                              #when the number of guesses is equal to 0
        print ("You lose")                                              
        print ("The word was:", secret)                                           #print the word

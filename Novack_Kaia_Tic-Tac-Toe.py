'''
┌───────────────────────────────────────────────────────────────────────────┐
│                               Tic-Tac-Toe                                 │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: K.Novack                                                            │
│ Log: 11/31/2024 - Finished product 1.0                                    |                                      
│ Bugs: n/a                                                                 │
│ Description: Asks a user to play tic-tac-toe and allows them to play with |
| one or two players. This code asks the user to input a number and checks  |
| if that spot is available. Lastly, the code checks if someone has won or  |
| if it is a tie, prints the score if someone wins, and then asks the user  |
| if they want to play again.                                                |
└───────────────────────────────────────────────────────────────────────────┘
'''

'''
1. Welcome! Do you want to play tic-tac-toe
2. 1 or 2 players?
3. Determine x or O
4. Draw the Board/Label coordinates
5. Loop 9 times (until board is filled) or break
6. Ask player 1 where they want to go
7. If exists prior turn -- then 'spot taken, go somewhere else'
8. Check if someone has won
8b. Display the Board
9. Player 2 (either a user or machine)
10. ...if machine --- random --- if spot it chose --- choose another random
11. If someone wins say player 1 or player 2 win
12. Do you want to play again?

check for bugs when actually coding
'''
import sys                                                                                                          #import the sys library
import random                                                                                                       #import the random library


def board(box):                                                                                                     #creates a function for the board called board
    '''
    Creates the box

    Args:
    box
    
    Returns:
        str: package type
    '''
    for i in range(len(box)):                                                                                       #for every 'x' value, add it to the box
        for j in range(len(box[i])):                                                                                #then for every 'y' value, add it to the box
            print(box[i][j], end=' ')                                                                               #print 'x', 'y'
        print(" ")                                                                                                  #print a space between each number

def box_point_entered(box, user_or_bot, XO):                                                                        #creates a function for the player or bot to choose where they want to go
    '''
    Sets the point the user enters as X or O, or allows the bot to enter O and updates the box with the point the user enters

    Args:
        box, user_or_bot, XO
    '''
    if user_or_bot == "user":                                                                                       #if it is the users turn
        print("It is now player", XO,"'s turn")                                                                     #print which players turn it is
    else:                                                                                                           #if it is not a user who is playing
        print("It is now the bot's turn")                                                                           #print that it is the bot's turn
    go = True                                                                                                       #set the variable go equal to True
    while go:                                                                                                       #while go is True
        if user_or_bot == "user":                                                                                   #if it is the users turn
            final_play_one = input("Player please enter the number of the box you would like to play: ")            #ask the player to enter the number of the box they would like to play and makes it an integer
        else:                                                                                                       #if it is not a user who is playing
            final_play_one = random.choice(list("123456789"))                                                       #if it is the bot's turn

        if final_play_one == "1" and box[0][0] == 1:                                                                #if the spot is one
            box [0][0] = XO                                                                                         #the point is at the x,y point 0,0
            go = False                                                                                              #set go equal to false
        elif final_play_one == "2" and box[0][1] == 2:                                                              #if the spot is two
            box [0][1] = XO                                                                                         #the point is at the x,y point 0,1
            go = False                                                                                              #set go equal to false
        elif final_play_one == "3" and box[0][2] == 3:                                                              #if the spot is three
            box [0][2] = XO                                                                                         #the point is at the x,y point 0,2
            go = False                                                                                              #set go equal to false
        elif final_play_one == "4" and box[1][0] == 4:                                                              #if the spot is four
            box [1][0] = XO                                                                                         #the point is at the x,y point 1,0
            go = False                                                                                              #set go equal to false
        elif final_play_one == "5" and box[1][1] == 5:                                                              #if the spot is five
            box [1][1] = XO                                                                                         #the point is at the x,y point 1,1
            go = False                                                                                              #set go equal to false
        elif final_play_one == "6" and box[1][2] == 6:                                                              #if the spot is six
            box [1][2] = XO                                                                                         #the point is at the x,y point 1,2
            go = False                                                                                              #set go equal to false
        elif final_play_one == "7" and box[2][0] == 7:                                                              #if the spot is seven
            box [2][0] = XO                                                                                         #the point is at the x,y point 2,0
            go = False                                                                                              #set go equal to false
        elif final_play_one == "8" and box[2][1] == 8:                                                              #if the spot is eight
            box [2][1] = XO                                                                                         #the point is at the x,y point 2,1
            go = False                                                                                              #set go equal to false
        elif final_play_one == "9" and box[2][2] == 9:                                                              #if the spot is nine
            box [2][2] = XO                                                                                         #the point is at the x,y point 2,2
            go = False                                                                                              #set go equal to false
        else:                                                                                                       #if the spot is taken                                                    
            if user_or_bot == "user":                                                                               #if the spot is entered by a user
                print()                                                                                             #prints a line
                print("The options are right in front of your face! Choose one!")                                   #print The options are right in front of your face! Choose one!
                print()                                                                                             #prints a line

def three(box, XO):                                                                                                 #create a function to find three in a row named three
    '''
    Checks if the user or bot has three in a row

    Args:
        box, XO

    Returns:
        boolean: True
    '''
    if box [0][0] == XO and box [0][1] == XO and box [0][2] == XO:                                                  #if x or o gets three across the top                                                                               #tell the user who won that they won
        return True                                                                                                 #makes the function three true
    elif box [1][0] == XO and box [1][1] == XO and box [1][2] == XO:                                                #if the user achieves three across the middle
        return True                                                                                                 #makes the function three true
    elif box [2][0] == XO and box [2][1] == XO and box [2][2] == XO:                                                #if x or o gets three across the bottom
        return True                                                                                                 #makes the function three true  
    elif box [0][0] == XO and box [1][0] == XO and box [2][0] == XO:                                                #if x or o get three down the left side
        return True                                                                                                 #makes the function three true
    elif box [0][1] == XO and box [1][1] == XO and box [2][1] == XO:                                                #if the user gets three down the middle
        return True                                                                                                 #makes the function three true
    elif box [0][2] == XO and box [1][2] == XO and box [2][2] == XO:                                                #if the user gets three down the left side
        return True                                                                                                 #makes the function three true
    elif box [0][0] == XO and box [1][1] == XO and box [2][2] == XO:                                                #if x or o get three diagonal: top left, middle, and bottom right
        return True                                                                                                 #makes the function three true
    elif box [0][2] == XO and box [1][1] == XO and box [2][0] == XO:                                                #if x or o get three diagonal: top right, middle, bottom left
        return True                                                                                                 #makes the function three true                                                                                    #tell the user who won that they won

def play_game(box, user_or_bot):                                                                                    #creates a function for one player called play_game_one
    '''
    Allows the user to play tic-tac-toe with either one or two players

    Args:
        box, user_or_bot
    '''
    turn = random.choice(["p1", "p2"])                                                                              #randomly choose who goes first by selecting True or False
    counter = 0                                                                                                     #set the counter equal to 0
    while counter < 9:                                                                                              #if the counter is less than 9
        board(box)                                                                                                  #prints the box
        print()                                                                                                     #prints a space under the box
        if turn == "p1":                                                                                            #if the turn is p1
            box_point_entered(box, "user", "X")                                                                     #run box_point_entered for X
            if three(box, "X"):                                                                                     #if three in a row is completed by X
                board(box)                                                                                          #print the box
                print ("You win: Player 1")                                                                         #print that Player 1 wins
                break                                                                                               #break the inifinite loop
            turn = "p2"                                                                                             #set the turn equal to p2
            counter += 1                                                                                            #add 1 to the counter
        else:                                                                                                       #if turn is p2
            if user_or_bot == "user":                                                                               #if p2 is a user
                box_point_entered(box, "user", "O")                                                                 #run box_point_entered for O and the user
            else:                                                                                                   #if p2 is not a user
                box_point_entered(box, "bot", "O")                                                                  #run box_point_entered for O and bot
            if three(box, "O"):                                                                                     #if p2 gets three in a row
                board(box)                                                                                          #print the box
                print ("You win: Player 2")                                                                         #print that Player 2 wins
                break                                                                                               #break the infinite loop
            turn = "p1"                                                                                             #set the turn equal to p1
            counter += 1                                                                                            #add 1 to the counter
    if counter == 9:                                                                                                #if the counter is equal to 9
        board(box)                                                                                                  #print the board
        print("It's a tie")                                                                                         #print that it is a tie

def main():                                                                                                         #creates a main function
    '''
    Asks the user to play tic-tac-toe, and allows them to play with either one or two players
    '''
    while True:                                                                                                     #creates an infinite loop
        yay_nay = input("Do you want to play tic-tac-toe? (yes or no): ").lower()                                   #asks the player if they want to play tic-tac-toe
        if yay_nay.strip() == "no":                                                                                 #if the player enters no
            print ("Too bad so sad")                                                                                #prints too bad so sad
            sys.exit()                                                                                              #completely exits the code
        elif yay_nay.strip() == "yes":                                                                              #if the user enters yes
            print ("Yay!")                                                                                          #print Yay!
            break                                                                                                   #break the while True
        else:                                                                                                       #if the player does not enter yes or no
            print("I gave you two options choose one!")                                                             #tells the player to enter yes or no
    scoreX = 0                                                                                                      #sets the score for player X to 0
    scoreO = 0                                                                                                      #sets the score for player O to 0
    while True:                                                                                                     #creates another while True

        box = [                                                                                                     #helps to create the box
            [1,2,3],                                                                                                #creates the first line of the box
            [4,5,6],                                                                                                #creates the second line of the box
            [7,8,9]]                                                                                                #creates the third line of the box
        amount_player = input("Do you want to play with one or two players? ").lower()                              #asks the player if they want to play with one or two players
        if amount_player == "one" or amount_player == "1":                                                          #if the player wants to play with one (1) player
            print("You have selected one player")                                                                   #tell the user that they have selected one player
            play_game(box, "bot")                                                                                   #run the function play_game with a bot
        elif amount_player == "two" or amount_player == "2":                                                        #if the user chooses the play with two (2) players
            print("You have selected two player")                                                                   #tell the user that they have selected two players
            play_game(box, "user")                                                                                  #run the function play_game with users                   
        if three(box, "X"):                                                                                         #if the player X wins
            scoreX +=1                                                                                              #add one to their score
            print()                                                                                                 #prints a blank line
            print("Player 1:", scoreX)                                                                              #prints Player 1's score
            print("Player 2:", scoreO)                                                                              #prints Player 2's score
            print()                                                                                                 #prints a blank line
            continue                                                                                                #continues to the top of the while True loop
        if three(box, "O"):                                                                                         #if player O wins
            scoreO +=1                                                                                              #adds one to player O's score
            print()                                                                                                 #prints a blank line
            print("Player 1:", scoreX)                                                                              #prints Player 1's score
            print("Player 2:", scoreO)                                                                              #prints Player 2's score
            print()                                                                                                 #prints a blank line
            continue                                                                                                #continues to the while True
        elif three(box, 'XO') != "X" or three(box, 'XO') != "O":                                                    #if no one has one
            continue                                                                                                #continues to the top of the while True
        else:                                                                                                       #if the player does not enter one (1) or two (2)
            print ("Please enter one or two")                                                                       #tell the player to enter one or two
main()                                                                                                              #runs the main function

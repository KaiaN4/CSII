'''
┌───────────────────────────────────────────────────────────────────────────┐
│                                Battleship                                 │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: K.Novack                                                            │
│ Log: 5/1/2025 - Finished product 1.0                                      |                                      
│ Bugs: n/a                                                                 │
│ Description: Asks the user if they want to play battleship and then if    |
| they want to play against a user or bot. Then, the user places the ships, | 
| and then the second user or bot places the ships. The computer then       |
| randomly selects who shoots at the ships first and that user or bot goes. |
| If all of the ships are gone on one of the players' boards, then one of   |
| the users has won. The user will then choose if they want to play against | 
| a user or bot again.                                                      |
└───────────────────────────────────────────────────────────────────────────┘
'''


'''
1. Create 2 2D arrays
    a. Make each box a coordinate
2. Decide how you want to label the board
    a. Create variables for ships, hits, and misses
        i. O - ship
        ii. X - miss
        iii. + - hits
3. User or Bot
4. Put in the ships (user) - name ideas (Dots_on_board_user() and Dots_on_board_computer())
    a. Take in a specific point for the ships
        i. Make sure the point is on the board
    b. Repeat 4 times
5. Put in the ships (user2 or bot)
    a. User 2
        i. Take in specific coordinates
        ii. Repeat 4 times
    b. Bot
        i. Randomly choose 4 spots on the 2D array
6. Hide the boards
7. Decide who goes first
    a. Ex. random or someone in a specific player
8. Guessing the Spot
    a. If user's input is equal to user2's input, it is a hit
        i. Remove the ship
    b. If they are not equal, it is not a hit
    c. Keep going if there are still ships (dots on the board)
    d. Cannot be the same as a previous guess
9. Update the board
10. Display the score
    a. How many hits you have
11. End Game
    a. When user or user2 have guessed all of the 4 ships (there will be none left), end the game
'''
import sys
import random
import os
import time

coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
               [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
               [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
               [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
               [4, 0], [4, 1], [4, 2], [4, 3], [4, 4] ]
placements = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]

def print_board(board):
    '''
    A function to print the board

    Args:
        board
    '''  
    for i in range(len(board)):                                                                                       #for every 'x' value, add it to the box
        for j in range(len(board[i])):                                                                                #then for every 'y' value, add it to the box
            print(board[i][j], end=' ')                                                                               #print 'x', 'y' 
        print("")                                                                           

def open_spots(board, user_or_bot):
    '''
    Allows the user to place ships and makes sure that the spots are open and on the board

    Args:
        board, user_or_bot
    '''  
    plays = []                                                                                                    #make a list for the plays a user wants to make
    count = 0                                                                                                     #sets the count equal to 0 because the user can only place 5 ships
    while count < 5:                                                                                              #while the count is less than 0
        if user_or_bot == "user":                                                                                 #if the user chose to play against another user
            print_board(board)
            final_play_one = input("Please enter the spot you would like to place a ship: ")                      #asks the user to place a ship
            
        else:
            final_play_one = str(random.randint(1, 25))                                                           #the bot chooses a random spot on the board
        
        if final_play_one not in placements or final_play_one in plays:                                           #if the spot has already been chosen or the spot is not on the board
            if user_or_bot == "user":
                print()                                                                                           #prints a line
                print("The options are right in front of your face! Choose one!")                                 #print The options are right in front of your face! Choose one!
                print() 

        else:                                                                
            coordinate = coordinates[placements.index(final_play_one)]                                            #converts the point the user put into coordinate points
            board[coordinate[0]][coordinate[1]] = "🚢"                                                           #sets the coordinates equal to a ship                             
            count += 1
            plays.append(final_play_one)                                                                          #adds the point to a list so the user does not enter it again
        
    return plays

def place_ships(board1, board2, user_bot):                                                                        
    '''
    Allows the user to place ships and switches turns after player 1 has entered 5 ships

    Args:
        board1, board2, user_bot
    '''    
    print("It is now player 1's turn")
    plays1 = open_spots(board1, "user")                                                                           #sets plays1 equal to the function to place the ships for player 1 (a user)
    print_board(board1)

    if user_bot == "user":                                                                                        #if the player chooses to play against another user
        time.sleep(2)
        os.system('cls')
        print("It is now Player 2's turn")
        plays2 = open_spots(board2, "user")                                                                       #sets plays2 equal to the function to place the ships for player 2 (a user)
        print_board(board2)
        time.sleep(2)
        os.system('cls')
    else:                                                                                                         #if the bot is playing
        print("The bot is now placing its ships")
        plays2 = open_spots(board2, "bot")                                                                        #sets plays2 equal to the function to place ships for a bot
    
    return plays1, plays2                                                                                         #returns the plays for later to know if a user finds a ship

def find_ships(board3, board4, plays1, plays2, user_or_bot):
    '''
    Allows the user to try and find the other player's ships

    Args:
        board3, board4, plays1, plays2, user_or_bot
    '''  
    p1shots = []
    p2shots = []
    botshots = placements[:]                                                                                      #creates the same list as placements, but makes it separate
    turn = random.randint(0, 1)                                                                                   #makes the turn between an even an odd integer to make the turn switching easier
   


    while plays1 and plays2:
        if turn % 2 == 0:                                                                                         #the remeainder of the turn, to tell whose turn it is (remainder 0 means even and remainder 1 odd)
            player = 'P1'
            plays = plays2            
            board = board4            
            shots = p1shots           
            print_board(board4)
            shot = input("P1, enter the number of the spot you would like to guess: ")                                                                                              #break the inifinite loop
        else:
            plays = plays1  
            board = board3
            shots = p2shots

            if user_or_bot == "user":
                player = 'P2'
                print_board(board3)
                shot = input("P2, enter the number of the spot you would like to guess: ")
            else:
                player = 'Bot'
                shot = random.choice(botshots)                                                                   #allows the bot to randomly choose a space
                botshots.remove(shot)                                                                            #removes the spot from the list so the bot does not choose it again
                print_board(board3)

        if shot in shots or shot not in placements:                                                              #if the space has already been guessed or not on the board
            print()
            print("Please enter a valid space!")
            continue
        elif shot in plays:                                                                                      #if the shot is in the other player's list of boat spots
            print()
            print(f"{player} got a hit!")                                                                        #the player got a hit
            plays.remove(shot)                                                                                   #removes the shot because that ship has been hit
            coordinate = coordinates[placements.index(shot)]                                                     #find the coordinate of the spot the user entered
            board[coordinate[0]][coordinate[1]] = "💥"                                                           #set the coordinate equal to an exploding emoji
        else:
            print()
            print(f"{player} missed:(")                                                                          #the player missed if the spot is not in plays
            coordinate = coordinates[placements.index(shot)]                                                     #find the coordinate of the input
            board[coordinate[0]][coordinate[1]] = "🌊"                                                           #set the spot equal to a wave
        shots.append(shot)                                                                                       #add the spot to the shots list so the user does not enter the same point more than once
        turn += 1                                                                                                #adds 1 to the turn to switch players
        time.sleep(1)
        os.system('cls')



    if plays1 == []:                                                                                            #if plays1 does not have any more ships in the list
        print_board(board3)
        print_board(board4)
        print ("Player 2 wins!")                                                                                #player 2 wins
    else:                                                                                                       #if plays2 is empty
        print_board(board4)
        print_board(board3)
        print ("Player 1 wins!")                                                                                #player 1 wins

def user_play(board1, board2, board3, board4):
    '''
    Organizes the functions for if the player selects to play against a user

    Args:
        board1, board2, board3, board4
    ''' 
    plays1, plays2 = place_ships(board1, board2, "user")                                                        #sets the plays of both users equal to the place ships function
    find_ships(board3, board4, plays1, plays2, "user")                                                          #allows both users to find ships

def bot_play(board1, board2, board3, board4):              
    '''
    Organizes the functions for if the player selects to play against a bot

    Args:
        board1, board2, board3, board4
    ''' 
    plays1, plays2 = place_ships(board1, board2, "bot")                                                        #sets the plays of the user and the bot equal to the place ships function
    find_ships(board3, board4, plays1, plays2, "bot")                                                          #allows the user to find ships, and also the bot

def main():
    '''
    Sets up the game by asking the user if they want to play, if they want to play against another user or a bot, and then plays the game

    Args:
        n/a
    ''' 
    board1 = [
        [" 1"," 2"," 3"," 4"," 5"],
        [" 6"," 7"," 8"," 9","10"],
        ["11","12","13","14","15"],
        ["16","17","18","19","20"],
        ["21","22","23","24","25"]
    ]
    board2 = [
        [" 1"," 2"," 3"," 4"," 5"],
        [" 6"," 7"," 8"," 9","10"],
        ["11","12","13","14","15"],
        ["16","17","18","19","20"],
        ["21","22","23","24","25"]
    ]
    board3 = [
        [" 1"," 2"," 3"," 4"," 5"],
        [" 6"," 7"," 8"," 9","10"],
        ["11","12","13","14","15"],
        ["16","17","18","19","20"],
        ["21","22","23","24","25"]
    ]
    board4 = [
        [" 1"," 2"," 3"," 4"," 5"],
        [" 6"," 7"," 8"," 9","10"],
        ["11","12","13","14","15"],
        ["16","17","18","19","20"],
        ["21","22","23","24","25"]
    ]

    while True:
        play_game = input("Do you want to play battleship? (yes/no): ").lower()
        
        if play_game == "yes" or play_game == "y":
            print("YAYAYAYAYAYA")
            break
        elif play_game == "no" or play_game == "n":
            print("BYE!")
            sys.exit()                                                                                    #manually exits the code
        else:
            print("Please enter yes or no!")
            continue
    while True:
        user_bot = input("Do you want to play against another user or a bot?: ").lower()
        
        if user_bot == "user":
            user_play(board1, board2, board3, board4)                                                    #plays the function of the user versus user
        elif user_bot == "bot":
            bot_play(board1, board2, board3, board4)                                                     #plays the function of a user versus bot
        else:
            print("Please enter user or bot!")

main()
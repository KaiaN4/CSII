'''
┌───────────────────────────────────────────────────────────────────────────┐
│                               GCDS Postoffice                             │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Kaia Novack                                                         │
│ Log: 9/26/24 - Finished product version 1.0                               │                                                            
│ Description: Acts as a post office so that a user can input the           |
| dimensions of their package and the to and from zipcodes, and prints out  |
| the final cost                                                            |
| Bugs: If the user puts in a number with a decimal for either zipcode      |
| Features: None.                                                           |
└───────────────────────────────────────────────────────────────────────────┘
'''

def getPostageType(length, height, thickness):                                                           #creates a function called getPostageType
    '''
    Sets values for the different postage types that a user may enter

    Args:
        length, height, and thickness (int): the length around a package, the height of a package, and the thickness of a package

    Returns:
        str: package type
    '''

    #Regular_Post_Card:
    if ((height >= 3.5 and height <= 6) and (length >= 3.5 and  length <= 4.25) and (thickness >= .007 and thickness <= .015)): #creates values the item has to fit in to be a regular post card
        return "Regular Post Card"                                                                       #if the variables meet this criteria it is a regular post card

    #Large_Post_Card:
    elif ((height > 6 and height < 11.25) and (length > 4.25 and length < 6) and (thickness >= .007 and thickness <= .015)): #creates values the item has to fit in to be a large post card
        return "Large Post Card"                                                                         #if the variables meet this criteria it is a large post card

    #Envelope:
    elif ((height >= 5 and height <= 11.5) and (length >= 3.5 and length <= 6.125) and (thickness > .016 and thickness < .25)): #creates values the item has to fit in to be an envelope
        return "Envelope"                                                                                #if the variables meet this criteria it is an envelope

    #Large_Envelope:
    elif ((height >= 11 and height <= 18) and (length > 6.125 and length < 24) and (thickness >= .25 and thickness <= .5)): #creates values the item has to fit in to be a large envelope
        return "Large Envelope"                                                                         #if the variables meet this criteria it is a large envelope

    #Package:
    elif (length+2*(height+thickness) <= 84):                                                           #creates values the item has to fit in to be a package
        return "Package"                                                                                #if the variables meet this criteria it is a package

    #Large_Package:
    elif (length+2*(height+thickness) > 84 and length+2*(height+thickness) <= 130):                     #creates values the item has to fit in to be a large package
        return "Large Package"                                                                          #if the variables meet this criteria it is a large package

    #Unmailable: 
    else:                                                                                               #anything outside of these values
        return "Unmailable"                                                                             #print unmailable


def getZone(zip):                                                                                       #creates a new function named getZip
    '''
    Sets values for the different zipcodes a user could enter

    Args:
        zip (int): The number for which the user may send a package to or from

    Returns:
        int: zone
    '''
    if zip >= 1 and zip <= 6999:                                                                        #if zip is between 1 and 6999
        return 1                                                                                        #return zone 1
    
    elif zip >= 7000 and zip <= 19999:                                                                  #if zip is between 7000 and 19999
        return 2                                                                                        #the zone is 2
    
    elif zip >= 20000 and zip <= 35999:                                                                 #if zip is between 20000 and 35999
        return 3                                                                                        #the zone is 3
    
    elif zip >= 36000 and zip <= 62999:                                                                 #if zip is between 36000 and 62999
        return 4                                                                                        #the zone is 4

    elif zip >= 63000 and zip <= 84999:                                                                 #if zip is between 63000 and 84999
        return 5                                                                                        #the zone is 5

    elif zip >= 85000 and zip <= 99999:                                                                 #if zip is between 85000 and 99999
        return 6                                                                                        #the zone is 6


def getCost(postage_type, total_distance):
    '''
    Sets values for the different postage types that a user may enter

        Args:
            postage_type(str) and total_distance(int): The values that are being returned from getPostageType and getZone

        Returns:
            int: final cost
    '''
    if postage_type == "Regular Post Card":                                                              #if getPostageType is regular post card
        return .20 + .03*total_distance                                                                  #the cost is 0.2 plus .03*total_distance
    
    elif postage_type == "Large Post Card":                                                              #if getPostageType is large post card
        return .37 + .03*total_distance                                                                  #the cost is 0.37 plus .03*total_distance

    elif postage_type == "Envelope":                                                                     #if getPostageType is envelope
        return .37 + .04*total_distance                                                                  #the cost is 0.37 plus .04*total_distance

    elif postage_type == "Large Envelope":                                                               #if getPostageType is large envelope
        return .60 + .05*total_distance                                                                  #the cost is 0.6 plus .05*total_distance

    elif postage_type == "Package":                                                                      #if getPostageType is package
        return 2.95 + .25*total_distance                                                                 #the cost is 2.95 plus .25*total_distance

    elif postage_type == "Large Package":                                                                #if getPostageType is large package
        return 3.95 + .35*total_distance                                                                 #the cost is 3.95 plus .35*total_distance


def main():                                                                                              #creates a main function
    '''
    Asks the user for values of length, height, thickness, zipcode to and from. tThen plugs them into the functions getZone, getPostageType, and getCost.

        Args:
            none

        Print:
            getCost(int): final cost
    '''
    while True:                                                                                          #creates an infinite loop
        dimensions = input("enter length, height, thickness, zipcode where you are mailing from, zipcode where you are mailing to: ").split(",") #asks the user about their package and the zipcodes they are mailing away from and to, splitting each with a comma
        if len(dimensions) != 5:                                                                         #if the length of dimensions does not equal 5
            print ("Please enter 5 perameters!")                                                         #tell the user to enter 5 perameters
            continue                                                                                     #restarts the while True
        else:                                                                                            #if there are 5 perameters
            try:                                                                                                 #attempts the following code to check for user input
                length = float(dimensions[0])                                                                    #length is the first term in dimensions, set to a float
                height = float(dimensions[1])                                                                    #height is the second term in dimensions, set to a float
                thickness = float(dimensions [2])                                                                #thickness is the third term in dimensions, set to a float
                away_zip = int(dimensions [3])                                                                   #away is the fourth term in dimensions, set as an integer
                to_zip = int(dimensions [4])                                                                     #to is the fifth term in dimensions, set as an integer

                postage_type = getPostageType(length, height, thickness)                                         #sets postage_type to the function getPostageType of the height, length, and thickness
                
                if postage_type == "Unmailable":                                                                 #if the postage type is unmailable
                    print ("Unmailable")                                                                         #print unmailable
                    continue                                                                                     #restarts the while true 

                elif 1 < away_zip < 999999 or 1 < to_zip < 999999:                                               #if get zip is between 1 and 99999
                    total_distance = abs(getZone(away_zip)-getZone(to_zip))                                      #the total distance is equal to the absolute value of away - to
                else:                                                                                            #if the zipcode is not between 1 and 99999
                    print("We cannot mail your package to your zipcode")                                         #print we cannot mail your package to your zipcode
                    continue                                                                                     #mrestarts the while True

                total_cost = (getCost(postage_type, total_distance))                                             #print the cost from the function getCost with the variables postage_type and total_distance
                final_cost = round(total_cost, 2)                                                                #rounds the total cost to two decimals
                formatted_total_cost = str(final_cost).lstrip("0")                                               #formats the final_cost to remove the leading 0 in front of a decimal point
                print(formatted_total_cost)                                                                      #prints the total cost
                break                                                                                    #manually ends the while True loop
            except (ValueError):
                print("That's not a number dumbo")                                                       #if there is a Value Error

main()                                                                                                   #run the main function
#  File: sumMaze.py
#  Description: HW8 - Traversing a maze using DFS & ending with a requested sum
#  Student's Name: Shan Deng
#  Student's UT EID: SD33857
#  Course Name: CS 313E 
#  Unique Number: 50739
#
#  Date Created: 4/18/19
#  Date Last Modified: 4/18/19

import copy

#Defines the State class that holds the state of the Maze and details of the maze
class State:

    #Initializes instance variables
    grid = []
    pathHist = []
    sRow = None
    sCol = None
    eRow = None
    eCol = None
    currentSum = 0
    goalSum = 0

    #When printed, Stat just returns a neat grid of the maze
    def __str__(self):
        return ('      ' +('\n      '.join([''.join(['{:4}'.format(item) for item in row]) 
          for row in self.grid])))

#Checks if a move could be made in a cardinal direction
def isValidMove(thisState, move):

    #Returns True if movement can be made; False if not
    if move == 'u':
        if thisState.sRow == 0 or thisState.grid[thisState.sRow - 1][thisState.sCol] == 'X':
            return False
        else:
            return True    

    if move == 'd':
        if thisState.sRow == (len(thisState.grid[0]) - 1) or thisState.grid[thisState.sRow + 1][thisState.sCol] == 'X':
            return False
        else:
            return True

    if move == 'l':

        if thisState.sCol == 0 or thisState.grid[thisState.sRow][thisState.sCol - 1] == 'X':
            return False
        else:
            return True

    if move == 'r':

        if thisState.sCol == (len(thisState.grid) - 1) or thisState.grid[thisState.sRow][thisState.sCol + 1] == 'X':
            return False
        else:
            return True

#Method used to find the path through the maze using DFS
def solve(thisState):

    #Updates the current sum & grid of the state
    thisState.currentSum += int(thisState.grid[thisState.sRow][thisState.sCol])
    thisState.grid[int(thisState.sRow)][int(thisState.sCol)] = 'X'

    #Mandatory outputs for visual validation    
    print ("   Grid:")
    print (thisState)
    print("   history: " + str(thisState.pathHist))
    print("   start point: (" + str(thisState.sRow) + "," + str(thisState.sCol) +")")
    print("   sum so far: " + str(thisState.currentSum))
    print()
    print("Is this a goal state?")

    #If we have the correct total...
    if thisState.currentSum == thisState.goalSum:

        #...AND are at the desired end point - Return the path as a success!
        if thisState.sCol == thisState.eCol and thisState.sRow == thisState.eRow:
            print ("Solution found!")
            return thisState.pathHist

        #Otherwise, if we're still not at the end point, then we've failed, and need to try another path
        else:
            print("No. Target Missed: abandoning path")
            return None

    #If we've overshot the correct total - Keep looking through the maze
    elif thisState.currentSum > thisState.goalSum:
        print ("No. Target exceeded:  abandoning path")
        return None

    #If we have less than the correct total - Keep looking through the maze        
    else:

        #Checks if we can move up
        print("No.  Can I move up?")
        if isValidMove(thisState, 'u'):

            #If we can, then check the path...
            print("Yes!")
            print()

            #Create a new State object that's similar to the old one
            newState = copy.deepcopy(thisState)

            #Update the row parameter
            newState.sRow -= 1

            #Make sure the pointers for the lists are also not pointing at the same list
            newState.pathHist = thisState.pathHist.copy()

            #Update the pathHistory list
            newState.pathHist.append(int(newState.grid[newState.sRow][newState.sCol]))
            print("Problem is now:")

            #Continue down the maze
            result = solve(newState)

            #If the result was a success - return the success through the rest of the recursion and stop checking!
            if result != None:
                return result

        #Otherwise, checks the other cardinal directions with the same logic, if the previous path did not return as success
        print("No.  Can I move down?")
        if isValidMove(thisState, 'd'):
            print("Yes!")
            print()
            newState = copy.deepcopy(thisState)
            newState.sRow += 1
            newState.pathHist = thisState.pathHist.copy()
            newState.pathHist.append(newState.grid[int(newState.sRow)][int(newState.sCol)])
            print("Problem is now:")
            result = solve(newState)
            if result != None:
                return result

        #Same thing but checks left movement
        print("No.  Can I move left?")
        if isValidMove(thisState, 'l'):
            print("Yes!")
            print()
            newState = copy.deepcopy(thisState)
            newState.sCol -= 1
            newState.pathHist = thisState.pathHist.copy()
            newState.pathHist.append(newState.grid[int(newState.sRow)][int(newState.sCol)])
            print("Problem is now:")
            result = solve(newState)
            if result != None:
                return result

        #Same thing but checks right movement
        print("No.  Can I move right?")
        if isValidMove(thisState, 'r'):
            print("Yes!")
            print()
            newState = copy.deepcopy(thisState)
            newState.sCol += 1
            newState.pathHist = thisState.pathHist.copy()
            newState.pathHist.append(newState.grid[int(newState.sRow)][int(newState.sCol)])
            print("Problem is now:")
            result = solve(newState)
            if result != None:
                return result

        #If none of these paths work, then return none and try a different path in an earlier step
        print("Couldn't move in any direction.  Backtracking.")
        return None

#Extracts the grid from the given parameters in the text file to reduce code in main
def createMaze(textfile):
    with open(textfile, "r") as mazeFile:
        firstRow = True
        gridMap = []

        #For each line in the maze file
        for line in mazeFile:
            #Skip the first row
            if firstRow:
                firstRow = False

            #Save all of the lines as given in a 2D list
            else:
                data = line.split()
                gridMap.append(data)

    #return the 2D list representation of the grid
    return gridMap

def main():

    #Creates the maze from the text file
    myMaze = createMaze("mazedata.txt")

    #Extracts maze details from the first line of the text file
    mazeFile = open("mazedata.txt", "r")
    line = mazeFile.readline()
    details = line.split()
    targetValue = details[0]
    start_row = details[3]
    start_col = details[4]
    end_row = details[5]
    end_col = details[6]

    #Create a new State object
    thisState = State()

    #Save maze details into the initial State object
    thisState.grid = myMaze
    thisState.sRow = int(start_row)
    thisState.sCol = int(start_col)
    thisState.eRow = int(end_row)
    thisState.eCol = int(end_col)
    thisState.goalSum = int(targetValue)
    thisState.pathHist.append(thisState.grid[int(start_row)][int(start_col)])

    #Check if the State/Maze can be solved given the parameters.
    result  = solve(thisState)

    #If it can be solved, print out the path
    if result == None:
      print("No solution exists")
    else:
      print("The solution is: " + str(result))

#Calls the main
main()




                

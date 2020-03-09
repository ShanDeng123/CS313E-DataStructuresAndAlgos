#  File: RPG.py
#  Description: Homework 3 - Roleplays a card game of War
#  Student's Name: Shan Deng
#  Student's UT EID: SD33857
#  Course Name: CS 313E 
#  Unique Number: 50739
#
#  Date Created: 2/17/19
#  Date Last Modified: 2/17/19

import random

class Card:

    #Initializing Storage Variables
    strSuit = ''
    strRank = ''

    #Dictionary for Rank conversions for war
    allVals = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    #Dummy variable to be overridden
    intVal = 0

    #All Cards need to be given a suit and a ranking value (2-A) in order to exist
    def __init__(self, Suit, Rank):

        #When initialized, cards will take in their suit and a ranking value (2-A)
        self.strSuit = Suit
        self.strRank = Rank

        #Ranking value will all be converted into numerical values based upon previous dictionary
        self.intVal = self.allVals.get(Rank)

    #When used as a string, cards will return their suit and rank like "3C" for 3 of clubs    
    def __str__(self):

        #All cards will be pinted with their Suit, followed by their rank, in a format of 3 spaces, centered right
        strCard = ''
        strCard = str("{:>3}".format(self.strRank + self.strSuit))
        return strCard

class Deck:
    ##Defines Valid Suit & Ranks for Cards
    allSuits = ['C','D','H','S']
    allRanks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
 
    #Initialized storage variable
    finalDeck = []

    #When a new deck is made, it'll hold one copy of every possible card.
    def __init__(self):
        #Creates a new deck of cards - One with every suit having all 13 ranks
        for suit in self.allSuits:
            for rank in self.allRanks:
                self.finalDeck.append(Card(suit,rank))

    #When a deck is printed, it returns a string of all cards in deck
    def __str__(self):
        
        #initialize storage variable
        testStr = ' '

        #stores out lines of 13 cards in string variable
        line = 0
        size = 13

        #makes sure that no unnecessary lines are printed - variable deck sizes caused by war will have variable lines
        while len(self.finalDeck) > (line * size):
            
            for card in self.finalDeck[(line * size):(line + 1) * size]:
                testStr += (str(card) + ' ')
            testStr += '\n '
            line += 1

        #returns final string variable
        return testStr

    #Method to shuffle the deck
    def shuffle(self):

        #Debugging code given by Bulko
        random.seed(15)
        #shuffles itself
        random.shuffle(self.finalDeck)

    #Deals out cards from the top of the deck, down to the bottom
    def dealOne(self, playerHand):
        #removes the top card from itself and gives it to the stated player's hand; Also increases that player's hand total by 1
        playerHand.hand.append(self.finalDeck[0])
        playerHand.handTotal =+ 1
        del self.finalDeck[0]
        
            
class Player:

    #When a player is created, they will start off with 0 cards
    def __init__(self):

        #Initializes storage/default variables
        self.hand = []
        self.handTotal = 0

    #returns a string of all cards in hand *Same code for string in deck
    def __str__(self):

        #initialize storage variable
        handStr = ' '

        #stores out lines of 13 cards in string variable
        line = 0
        size = 13

        #makes sure that no unnecessary lines are printed - variable deck sizes caused by war will have variable lines
        while len(self.hand) > (line * size):
            for card in self.hand[(line * size):(line + 1) * size]:
                handStr += (str(card) + ' ')

            #Used to add new lines to perfectly match Bulko's output to satisfy his ego and his grading nazis; Has no functionality beyond fitting a set visual kink.
            #New lines are started after each line of 13 cards
            if(len(self.hand) >= ( (line + 1) * size)):
                handStr += '\n '
            line += 1

        #returns string of the final list of cards in hand
        return handStr

    #Boolean used to check if the player's hand is not empty *Used at the end of the game to determine the winnner
    def handNotEmpty(self):
        
        #checks if the player's hand is not empty
        if (len(self.hand) != 0):
            return True
        return False

#General method used to play a card game
def playGame(deck, p1, p2):

    #Starting Text
    print()
    print()
    print('Initial hands:')
    print('Player 1: ')
    print(p1)
    print()
    print('Player 2: ')
    print(p2)

    #All rounds start as 1 and will increase by 1 for each loop of card-comparisons
    roundCount = 1

    #Plays automatically until someone runs out of cards
    while (len(p1.hand) > 0 and len(p2.hand) > 0):
        print()
        print()
        print('ROUND ' + str(roundCount) + ': ')
        print('Player 1 plays: ' + str(p1.hand[0]))
        print('Player 2 plays: ' + str(p2.hand[0]))
        print()

        #If the card ranks are the same, go to war
        if (p1.hand[0].intVal == p2.hand[0].intVal):

            #war point marker is made in case of mutiple wars.
            warPt = 0

            #While the cards at war are the same in rank (multiple in case cards war more than once)
            while (p1.hand[warPt].intVal == p2.hand[warPt].intVal):

                #First check to see if both players have enough cards for war - if not, they lose and concede all of their cards
                if(len(p1.hand) < (warPt + 5)):
                    print('Player 1 ran out of cards!!!')
                    p2.hand.extend(p1.hand[0:])
                    del p1.hand[0:]
                    p1.handTotal = len(p1.hand)
                    p2.handTotal = len(p2.hand)

                    #War immediately stops if not enough cards and after cards are conceded
                    #Causing the length of the deck to run to 0 instantly ends the game as well
                    break

                #Same check for player 2
                elif(len(p2.hand) < (warPt + 5)):
                    print('Player 2 ran out of cards!!!')
                    p1.hand.extend(p2.hand[0:])
                    del p2.hand[0:]
                    p1.handTotal = len(p1.hand)
                    p2.handTotal = len(p2.hand)

                    break

                #Otherwise, the war continues, and cards are battled
                print('War starts: ' + str(p1.hand[warPt]) + ' = ' + str(p2.hand[warPt]))

                
                #First 3 cards after the war cards are put face down
                for fdCard in range(warPt + 1, warPt + 4):
                    print('Player 1 puts ' + str(p1.hand[fdCard]) + ' face down')
                    print('Player 2 puts ' + str(p2.hand[fdCard]) + ' face down')

                #4th card after the war-card is used to decide the war from both decks
                print('Player 1 puts ' + str(p1.hand[(warPt + 4)]) + ' face up')
                print('Player 2 puts ' + str(p2.hand[(warPt + 4)]) + ' face up')
                print()

                #War point marker moves up 4 to allow for additional wars
                warPt += 4

                #Once a player wins the war, all of their cards will go to the opponent
                #Player 1's cards will be added to the bottom of the respective deck first, followed by Player 2's cards
                if (p1.hand[warPt].intVal > p2.hand[warPt].intVal):
                    print('Player 1 wins round ' + str(roundCount) + ': ' + str(p1.hand[warPt]) + ' > ' + str(p2.hand[warPt]))
                    for riskedCard in range(0,warPt + 1):
                        p1.hand.append(p1.hand[riskedCard])
                    for riskedCard in range(0,warPt + 1):
                        p1.hand.append(p2.hand[riskedCard])

                    #Cards are removed after they are placed at the bottom of the respective deck
                    del p1.hand[0:warPt + 1]
                    del p2.hand[0:warPt + 1]

                    #Hand Totals are changed
                    p1.handTotal = len(p1.hand)
                    p2.handTotal = len(p2.hand)

                    #Round progresses and status summary is printed
                    roundCount += 1
                    print()
                    print('Player 1 now has ' + str(p1.handTotal) + ' card(s) in hand:')
                    print(p1)
                    print('Player 2 now has ' + str(p2.handTotal) + ' card(s) in hand:')
                    print(p2)

                    break

                  #Same process if p2 wins
                elif (p1.hand[warPt].intVal < p2.hand[warPt].intVal):
                    print('Player 2 wins round ' + str(roundCount) + ': ' + str(p2.hand[warPt]) + ' > ' + str(p1.hand[warPt]))
                    for riskedCard in range(0,warPt + 1):
                        p2.hand.append(p1.hand[riskedCard])
                    for riskedCard in range(0,warPt + 1):
                        p2.hand.append(p2.hand[riskedCard])
                    del p1.hand[0:warPt + 1]
                    del p2.hand[0:warPt + 1]
                    p1.handTotal = len(p1.hand)
                    p2.handTotal = len(p2.hand)

                    roundCount += 1
                    print()
                    print('Player 1 now has ' + str(p1.handTotal) + ' card(s) in hand:')
                    print(p1)
                    print('Player 2 now has ' + str(p2.handTotal) + ' card(s) in hand:')
                    print(p2)

                    break

        #If a war doesn't occur, simply compare starting cards and add/remove/progress as necessary
        elif (p1.hand[0].intVal > p2.hand[0].intVal):
            print('Player 1 wins round ' + str(roundCount) + ': ' + str(p1.hand[0]) + ' > ' + str(p2.hand[0]))
            p1.hand.append(p1.hand[0])
            p1.hand.append(p2.hand[0])
            del p1.hand[0]
            del p2.hand[0]
            p1.handTotal = len(p1.hand)
            p2.handTotal = len(p2.hand)

            roundCount += 1
            print()
            print('Player 1 now has ' + str(p1.handTotal) + ' card(s) in hand:')
            print(p1)
            print('Player 2 now has ' + str(p2.handTotal) + ' card(s) in hand:')
            print(p2)

        elif (p1.hand[0].intVal < p2.hand[0].intVal):
            print('Player 2 wins round ' + str(roundCount) + ': ' + str(p2.hand[0]) + ' > ' + str(p1.hand[0]))
            p2.hand.append(p1.hand[0])
            p2.hand.append(p2.hand[0])
            del p1.hand[0]
            del p2.hand[0]
            p1.handTotal = len(p1.hand)
            p2.handTotal = len(p2.hand)

            roundCount += 1
            print()
            print('Player 1 now has ' + str(p1.handTotal) + ' card(s) in hand:')
            print(p1)
            print('Player 2 now has ' + str(p2.handTotal) + ' card(s) in hand:')
            print(p2)

            
#Main method provided by Bulko
def main():

    cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
    print("Initial deck:")
    print(cardDeck)                 # print the deck so we can see that you built it correctly
    
    random.seed(15)                 # leave this in for grading purposes
    cardDeck.shuffle()              # shuffle the deck
    print("Shuffled deck:")
    print(cardDeck)                 # print the deck so we can see that your shuffle worked
    
    player1 = Player()              # create a player
    player2 = Player()              # create another player

    for i in range(26):             # deal 26 cards to each player, one at 
       cardDeck.dealOne(player1)    #   a time, alternating between players
       cardDeck.dealOne(player2)
    
    playGame(cardDeck,player1,player2)

    if player1.handNotEmpty():
        print("\n\nGame over.  Player 1 wins!")
    else:
        print("\n\nGame over.  Player 2 wins!")

    print ("\n\nFinal hands:")    
    print ("Player 1:   ")
    print (player1)                 # printing a player object should print that player's hand
    print ("\nPlayer 2:")
    print (player2)                 # one of these players will have all of the cards, the other none
    
main()

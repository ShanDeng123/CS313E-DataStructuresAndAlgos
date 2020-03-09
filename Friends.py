#  File: Friends.py
#  Description: Homework 7 - Replicating Facebook "friend" application
#  Student's Name: Shan Deng
#  Student's UT EID: SD33857
#  Course Name: CS 313E 
#  Unique Number: 50739
#
#  Date Created: 4/2/19
#  Date Last Modified: 4/2/19

#Recycled Node Class; Hold data on the node, and a pointer to the next node if relevant
class Node:
   def __init__(self,initData):
      self.data = initData
      self.next = None

#Getting Node Data/Pointer
   def getData(self):
      return self.data

   def getNext(self):
      return self.next

#Setting Node Data/Pointer
   def setData(self,newData):
      self.data = newData

   def setNext(self,newNext):
      self.next = newNext


#Defining the Linked List
class LinkedList:

#All Linked Lists have a head
   def __init__(self):
      self.head = None

   # Return a string representation of data suitable for printing.
   #    Long lists (more than 10 elements long) should be neatly
   #    printed with 10 elements to a line, one space between
   #    elements
   def __str__ (self):

      #Initialize a blank/storage string
      
      llString = '[ '

      #Initialize a count variable to add new lines every 10 nodes
      count = 0

      
      currentNode = self.head
      if currentNode == None:
         return llString
      while currentNode != None:
         llString += currentNode.getData().name + " "
         currentNode = currentNode.getNext()
         count += 1

      #If the node count is a multiple of 10, print a new line
         if count % 10 == 0:
            llString += "\n"

      #Formatting
      llString += "]"
      
      return llString

   # Search in an unordered list
   #    Return True if the item is in the list, False
   #    otherwise.
   def findUnordered (self, item): 

        found = False
        current = self.head

      #Searches through list - If the data in the Node matches the item, return true
        while current != None and not found:
            if current.getData().name == item:
                found = True
                
            else:
                current = current.getNext()

        return found

   # Search in an unordered list
   #    Return the user object if the user is in the list, None
   #    otherwise.
   def findUserUnordered (self, item): 

      found = False
      current = self.head

      #Searches through list - If the data in the Node matches the item, return true
      while current != None and not found:
         if current.getData().name == item:
            found = True
                
         else:
            current = current.getNext()
      if found:
         return current.getData()
      else:
         return None
      
   # Add an item to the beginning of the list
   #Add the given data as a new node & point to current head & reset head
   def addFirst (self, item):
      
      newHead = Node(item)
      newHead.setNext(self.head)
      self.head = newHead
      
   # Delete an item from an unordered list
   #    if found, return True; otherwise, return False
   def delete (self, item):

      found = False
      previous = None
      current = self.head

      #Searches through the list and returns True if found
      while current != None and not found:
         if current.getData() == item:
            found = True
         else:
            previous = current
            current = current.getNext()

        # if I get to this point, "current" points to the
        # item I want to delete
      if found:
         if previous == None:
            self.head = current.getNext()
         else:
            previous.setNext(current.getNext())

      return found

   #Checks if a username is already present within the list - If not, then add it
   def newInstance(self, command):
      name = command.split()[1]
      if self.findUnordered(name):
         print("    A person with name " + name + " already exists.")

      else:
         self.addFirst(User(name))
         print("    " + name + " now has an account.")

   #Checks if given usernames are valid within the linkedlist;
   #Returns True if Valid
   def nameExists(self, name1, name2):
      exist = True
      
      if not self.findUnordered(name1):
         print("    A person with name " + name1 + " does not currently exist.")
         exist = False
      
      elif not self.findUnordered(name2):
         print("    A person with name " + name2 + " does not currently exist.")
         exist = False

      return exist

   #Checks if two users in the list are friends
   def checkFriend(self, command):

      #Extracting usernames from the given command
      name1 = command.split()[1]
      name2 = command.split()[2]

      #Checks that names are not identical
      if name1 == name2:
         print("    A person cannot query him/herself.")
         
      else:
         #If the usernames are valid, look through one person's friend list
         #If the other person is on the list, then it can be inferred that
         #They are both friends.
         if self.nameExists(name1,name2):
            person1 = self.findUserUnordered(name1)
            if person1.friends.findUnordered(name2):
               print ("    " + name1 + " and " + name2 + " are friends.")

            else:
               print ("    " + name1 + " and " + name2 + " are not friends.")

class User:

   #All users have a name a friend linkedlist
   def __init__(self, personName):
      self.name = personName
      self.friends = LinkedList()

   #Prints out the user's friend list
   def friendsList(self):
      if self.friends.head == None:
         print("    " + self.name + " has no friends.")
      else:
         print("    " + str(self.friends))

   #Adds another user to the friend list
   def addFriend(self, other):

      #Checks if a user is trying to add itself
      if self.name == other.name:
         print("    A person cannot friend him/herself.")

      else:
         #If the users are already friends, do nothing
         if self.friends.findUnordered(other.name):
               print("    " + self.name + " and " + other.name + " are already friends.")

         #Otherwise, add them to each other's friend list
         else:
            self.friends.addFirst(other)
            other.friends.addFirst(self)
            print("    " + self.name + " and " + other.name + " are now friends.")

   #Removes users from each other's friend list
   def delFriend(self, other):

      #Checks if a user is trying to unfriend himself
      if self.name == other.name:
         print("    A person cannot unfriend him/herself.")

      else:
         #If a user can successfully delete another off of its friend list,
         #Delete the users off of each other's lists
         if self.friends.delete(other):
            other.friends.delete(self)
            print("    " + self.name + " and " + other.name + " are no longer friends.")

         #Otherwise, they must not be friends and so do nothing.
         elif not self.friends.delete(other):
            print("    " + self.name + " and " + other.name + " aren't friends, so you can't unfriend them.")

def main():

   #Initializes a linkedlist containing all users
    PersonList = LinkedList()
    
    with open("FriendData.txt","r") as hwFile:
        print()

       #For each line in the file..
        for command in hwFile:
            print("--> " + command.rstrip("\n"))

           #If contains "Person", it must mean to add a new user
            if "Person" in command:
               PersonList.newInstance(command)

            #If contains "List", it must mean to print the user's friend list
            elif "List" in command:
               name = command.split()[1]
               if PersonList.findUnordered(name):
                  person = PersonList.findUserUnordered(name)
                  person.friendsList()

            #If contains "Friend", it must mean for two users to become friends
            elif "Friend" in command:
               name1 = command.split()[1]
               name2 = command.split()[2]

               #First check if the users exist before trying to add them
               #to each others' friend list
               if PersonList.nameExists(name1,name2):
                  person1 = PersonList.findUserUnordered(name1)
                  person2 = PersonList.findUserUnordered(name2)
                  person1.addFriend(person2)

            #If contains "Unfriend", it must mean for two users to
            #stop being friends
            elif "Unfriend" in command:
               name1 = command.split()[1]
               name2 = command.split()[2]

               #First check if the users exist before trying to remove them
               #from each others' friend list
               if PersonList.nameExists(name1,name2):
                  person1 = PersonList.findUserUnordered(name1)
                  person2 = PersonList.findUserUnordered(name2)
                  person1.delFriend(person2)
     
            #If contains "Query", it must to check if a user exists
            elif "Query" in command:
               PersonList.checkFriend(command)

            #If contains "Exit", it must to stop the program
            elif "Exit" in command:
               print("    Exiting...")
               return

            print()

main()





               
               

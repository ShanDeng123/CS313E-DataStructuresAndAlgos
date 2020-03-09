#  File: LinkedLists.py
#  Description: Homework 6 - Develops a linked list
#  Student's Name: Shan Deng
#  Student's UT EID: SD33857
#  Course Name: CS 313E 
#  Unique Number: 50739
#
#  Date Created: 3/23/19
#  Date Last Modified: 3/23/19

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

   def __str__ (self):
               
      # Return a string representation of data suitable for printing.
      #    Long lists (more than 10 elements long) should be neatly
      #    printed with 10 elements to a line, two spaces between
      #    elements

#Initialize a blank/storage string
      
      llString = ''

#Initialize a count variable to add new lines every 10 nodes
      count = 0
      
      currentNode = self.head
      if currentNode == None:
         return llString
      while currentNode.getNext() != None:
         llString += currentNode.getData() + "  "
         currentNode = currentNode.getNext()
         count += 1

      #If the node count is a multiple of 10, print a new line
         if count % 10 == 0:
            llString += "\n"
            
      llString += currentNode.getData()

      return llString

     
   def addFirst (self, item):
      
      # Add an item to the beginning of the list
      #Add the given data as a new node & point to current head & reset head
      
      newHead = Node(item)
      newHead.setNext(self.head)
      self.head = newHead

   def addLast (self, item):

      # Add an item to the end of a list
      #Base case - 1st node then just add the node as the head
      if self.head == None:
         self.head = Node(item)
      #Otherwise, replace the last "None" pointer to redirect to this node,
      #and have this node point to None
      else:
         lastNode = self.head
         while lastNode.getNext() != None:
            lastNode = lastNode.getNext()
            
         lastNode.setNext(Node(item))

   def addInOrder (self, item):

      # Insert an item into the proper place of an ordered list.
      # This assumes that the original list is already properly
      #    ordered.

      #Base case- set new node as head if linkedlist is empty
      if self.head == None:
         self.head = Node(item)
         return

      #Otherwise, compare string values to determine where the Node needs to go
      previous = None
      current = self.head
      newNode = Node(item)

      while newNode.getData() > current.getData():

         if current.getNext() == None:
            current.setNext(newNode)
            return
         
         previous = current
         current = current.getNext()
      
      if previous == None:
         self.head = newNode
      else:   
         previous.setNext(newNode)
      
      newNode.setNext(current)

   def getLength (self):
      
      # Return the number of items in the list

      #Base case - empty list has 0 items
      if self.head == None:
         return 0

      #Length is just however many nodes exist
      nodeCount = 1
      nodePath = self.head
      while nodePath.getNext() != None:
         nodeCount += 1
         nodePath = nodePath.getNext()

      return nodeCount
        
   def findUnordered (self, item): 
        # Search in an unordered list
        #    Return True if the item is in the list, False
        #    otherwise.

        found = False
        current = self.head

         #Searches through list - If the data in the Node matches the item, return true
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

   def findOrdered (self, item): 
      # Search in an ordered list
      #    Return True if the item is in the list, False
      #    otherwise.
      # This method MUST take advantage of the fact that the
      #    list is ordered to return quicker if the item is not
      #    in the list.

      found = False
      current = self.head

      #Same process as the last search, but stops after the item value is not found in the valid position

      while current != None and item >= current.getData() and not found:
         if current.getData() == item:
            found = True
         else:
            current = current.getNext()

      return found

   def delete (self, item):
      # Delete an item from an unordered list
      #    if found, return True; otherwise, return False

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

   def copyList (self):

      # Return a new linked list that's a copy of the original,
      #    made up of copies of the original elements

      #Traverses list and copies the data found in each node into a new node
      newList = LinkedList()
      if self.head == None:
         return newList
      
      #Nodes are added at the end of the list not the start
      current = self.head
      while current != None:
         copyData = current.getData()
         newList.addLast(copyData)
         current = current.getNext()

      return newList
   
   def reverseList (self): 
        # Return a new linked list that contains the elements of the
        #    original list in the reverse order.

      #Same concept as the copy-list, but adds at the start of the list and not the end
      newList = LinkedList()
      if self.head == None:
         return newList

      current = self.head
      while current != None:
         copyData = current.getData()
         newList.addFirst(copyData)
         current = current.getNext()

      return newList


   def orderList (self): 
        # Return a new linked list that contains the elements of the
        #    original list arranged in ascending (alphabetical) order.
        #    Do NOT use a sort function:  do this by iteratively
        #    traversing the first list and then inserting copies of
        #    each item into the correct place in the new list.

      newList = LinkedList()
      if self.head == None:
         return newList

      current = self.head
      while current != None:
         copyData = current.getData()
         newList.addInOrder(copyData)
         current = current.getNext()

      return newList

   def isOrdered (self):
        # Return True if a list is ordered in ascending (alphabetical)
        #    order, or False otherwise

        #Checks the current list, and an ordered copy of that list, to see if they match
      orderedList = self.orderList()
      ordered = True
            
      current1 = self.head
      current2 = orderedList.head

      while current1 != None and current2 != None and ordered:
         if current1.getData() != current2.getData():
            ordered = False

         current1 = current1.getNext()
         current2 = current2.getNext()

      return ordered

   def isEmpty (self):
      #Checks if current list is empty
        return self.head == None

   def mergeList (self, b): 
      # Return an ordered list whose elements consist of the 
      #    elements of two ordered lists combined.
      
      mergedList = self
      current = b.head

      while current != None:
         mergedList.addFirst(current.getData())
         current = current.getNext()

      return mergedList.orderList()

   def isEqual (self, b):
      # Test if two lists are equal, item by item, and return True.
      equal = True

      #Parses through each list's data to see if they match.
      if self.head == None:
         if b.head == None:
            equal = True
         else:
            equal = False
         return equal

      current1 = self.head
      current2 = b.head
      
      if current1.getData() != current2.getData():
         equal = False
         return equal

      while True:
         if current1.getNext() == None or current2.getNext() == None:
            if current1.getNext() == current2.getNext():
               equal = True
            else:
               equal = False
            return equal
         equal = (current1.getNext().getData() == current2.getNext().getData())
         if not equal:
            return equal
         current1 = current1.getNext()
         current2 = current2.getNext()
   
   def removeDuplicates (self):
      # Remove all duplicates from a list, returning a new list.
      #    Do not change the order of the remaining elements.

      noDupes = LinkedList()

      currentNode = self.head
      while currentNode != None:

         ndNode = noDupes.head
         notDupe = True

         while ndNode != None:
            
            if ndNode.getData() == currentNode.getData():
               notDupe = False
            ndNode = ndNode.getNext()

         if notDupe:
            noDupes.addLast(currentNode.getData())
            
         currentNode = currentNode.getNext()

      return noDupes
                  


# Copy and paste the following after your class definitions for
# Nodes and LinkedLists.  Do NOT change any of the code in main()!

def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 

   print ("\n\n***************************************************************")
   print ("Test of orderList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto?")
   
   print ("   Original list:")
   print (planets)
   print ("   Ordered list:")
   orderedPlanets = planets.orderList()
   print (orderedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isOrdered:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Ordered? ", planets.isOrdered())
   orderedPlanets = planets.orderList()
   print ("   After ordering:")
   print (orderedPlanets)
   print ("   ordered? ", orderedPlanets.isOrdered())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)

main()

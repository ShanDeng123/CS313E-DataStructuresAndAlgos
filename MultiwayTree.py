#  File: MultiwayTree.py
#  Description: Homework 10 - Tree shape comparison (Isomorphism)
#  Student's Name: Shan Deng
#  Student's UT EID: SD33857
#  Course Name: CS 313E 
#  Unique Number: 50739
#
#  Date Created: 5/2/19
#  Date Last Modified: 5/2/19

class MultiwayTree:

  #All multiay Trees are created with a given string in the format of [root,[children]]
  def __init__(self, s):

    #self.val is the root in the string
    self.val = (s[1:s.index(',')])

    #Calls another function to extract the children in the string
    self.children = self.get_children(s)

    #Creates more trees using the children strings
    self.children = [MultiwayTree(c) for c in self.children]

  #Function to print out the tree in preorder format
  def preOrder(self):

    #Initialize string to hold all of the values in the tree
    x = ''

    #Adds each value & removes quotes from letters to match Bulko's formatting
    x += self.val.strip('"')

    #Adds spaces for Bulko's formatting
    x += ' ' 
    for child in self.children:
      #Recursively goes down the tree and adds in each value as it goes down
      x += child.preOrder()

    #Return the final string
    return x

  #return True if the tree "self" has the same structure as the
  #tree "other", "False" otherwise.
  def isIsomorphicTo(self,other):

    #Defaults to true
    status = True

    #Compares the # of children for each parent
    #If they're not the same, then the shapes must be different
    if len(self.children) != len(other.children):
      status = False
      return status
    else:

      #Recursively go down the tree performing the same function
      for nodeCount in range(len(self.children)):
        status = self.children[nodeCount].isIsomorphicTo(other.children[nodeCount])
        if not status:
          break

    return status

  #Function to extract the children from the given string
  def get_children(self, s):
    #Ignores the second and second-from-last brackets in order to isolate the children nodes
    s = s[s.index('[', 1) + 1:-2]

    #Initialize list of children
    children = []

    #Start blank string to find each child
    child = ''

    #Counts the number of open brackets
    #When the number of open and closed brackets hit 0
    #We've found an enclosed child
    
    cnt = 0
    skip = False
    for c in s:
      if skip:
        skip = False
        continue
      if c == '[':
        cnt = cnt + 1
      child = child + c
      if c == ']':
        cnt = cnt - 1

        #Append the enclosed child when count hits 0 and refresh the string
        if cnt == 0:
          children.append(child)
          child = ''
          skip = True
    return children


def main():
   #Read in the text file
  with open("MultiwayTreeInput.txt","r") as treeFile:
        print()

        #Count variable used to compare multiple trees
        treeNum = 1

        #List to hold trees to compare
        treeList = []

        #Each line in the file will be a tree
        for tree in treeFile:
           
           #Remove the \n from formatting
          tree = tree.strip('\n')
          print("Tree " + str(treeNum) + ":  " + str(tree))

          #Remove extra spaces
          tree = tree.replace(' ', '')

          #Create a new tree object from the given string
          bigTree = MultiwayTree(tree)

          #Print the preorder of that tree's values
          print("Tree " + str(treeNum) + " preorder:  " + bigTree.preOrder())

          #Append that tree to the overall list of trees
          treeList.append(bigTree)

          #For every 2 trees, compare the two for isomorphism
          if treeNum%2 == 0:
            if(bigTree.isIsomorphicTo(treeList[treeNum-2])):
              print()
              print("Tree " + str(treeNum-1) + " is isomorphic to Tree " + str(treeNum))
              print()
            else:
              print()
              print("Tree " + str(treeNum-1) + " is not isomorphic to Tree " + str(treeNum))
              print()

         #Extra print statements to match Bulko's formatting
          print()

          #Increase the count to continue to match formatting
          treeNum += 1

#Call main
main()

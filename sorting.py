#  File: sorting.py
#  Description: Homework 9 - Tests average runtime of different sorting operations
#  Student's Name: Shan Deng
#  Student's UT EID: SD33857
#  Course Name: CS 313E 
#  Unique Number: 50739
#
#  Date Created: 4/20/19
#  Date Last Modified: 4/20/19

#Imported stuff that bulko suggested
import random
import time
import sys
sys.setrecursionlimit(10000)

#Sorting algos from Bulko
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

#End of sorting algos from Bulko -------------------------------

#Takes in a quantity of nums to generate, type of sort, and type of list
#And creates the appropriate list type & runs the correct sort & returns the time
def sortTimer(numRange,sortType, listType):
   numList = []

   #Creates the appropriate list based on inputed param
   if listType == 'Random':
      for num in range(numRange):
         numList.append(random.randint(1,100000))
         
   elif listType == 'Sorted':
      for num in range(numRange):
         numList.append(random.randint(1,100000))
      mergeSort(numList)

   elif listType == 'Reverse':
      revList = []
      for num in range(numRange):
         numList.append(random.randint(1,100000))
      mergeSort(numList)
      while numList != []:
         revList.append(numList.pop())
      numList = revList

   elif listType == 'Almost sorted':
      for num in range(numRange):
         numList.append(random.randint(1,100000))
      mergeSort(numList)

      #Makes 1 random swap for every 10 nums
      for swap in range(int(numRange/10)):
         index1 = random.randint(0,(numRange-1))
         index2 = random.randint(0,(numRange-1))

         #Makes sure index numbers for swapping aren't the same
         while index1 == index2:
            index2 = random.randint(0,(numRange-1))
         numList[index1],numList[index2] = numList[index2],numList[index1]

   else:
      print("TypeError")

   #Runs the appropriate sorting method, times each sort, and calcs the elapsed time
   if sortType == 'b':  
      startTime = time.time()
      bubbleSort(numList)
      endTime = time.time()
      elapsedTime = endTime - startTime

   elif sortType == 'i':
      startTime = time.time()
      insertionSort(numList)
      endTime = time.time()
      elapsedTime = endTime - startTime

   elif sortType == 'm':
      startTime = time.time()
      mergeSort(numList)
      endTime = time.time()
      elapsedTime = endTime - startTime

   elif sortType == 'q':
      startTime = time.time()
      quickSort(numList)
      endTime = time.time()
      elapsedTime = endTime - startTime

   #Returns the elapsed time for the relevant sort
   return elapsedTime

#Returns average runtime of a sort - Holds params to pass down
def avgTimer(nRange, sType, listType):
   sortTime = []
   #Loops the sort-Time method 5 times
   for loop in range(5):
      sortTime.append(sortTimer(nRange,sType, listType))

   #returns the average of the 5 times
   return sum(sortTime)/len(sortTime)

#Defines the different numRange params to pass down
def difRanges(sType, listType):
   numRanges = [10,100,1000]
   typeTimes = []

   #Gets the average sort times for lists of size 10, 100, and 1000
   for num in numRanges:
      typeTimes.append(avgTimer(num, sType, listType))

   #Returns the average sort times for the set 3 numRanges
   return typeTimes

#Defines the different sortType params to pass down
def difSorts(listType):
   sortTypes = ['b','i','m','q']
   allAvgs = []
   for sort in sortTypes:
      allAvgs.append(difRanges(sort, listType))

   #returns a 2d list of sortTimes by different sort types
   return allAvgs
      

#Main
def main():

   #Defines the different kind of list structures we want to try to sort
   listTypes = ['Random', 'Sorted', 'Reverse', 'Almost sorted']

   #Defines the different types of sorts again for printing - May be redun, but too lazy to change
   sortTypes = ['bubbleSort', 'insertionSort', 'mergeSort', 'quickSort']

   #For each of type of list to test
   for lType in listTypes:

      #Print the basic format
      print("Input type = " + lType)
      print("                    avg time   avg time   avg time")
      print("   Sort function     (n=10)    (n=100)    (n=1000)")
      print("-----------------------------------------------------")

      #Get the 2D list of all the sort types and sort times using the given list format
      TypeData = difSorts(lType)

      #Defines an index for printing to identify what numbers correspond to what sort
      sortIndex = 0
      #For each list of times in the bigger list of sortTypes
      for avgTimes in TypeData:
         #Initialize a string to record data & Assign the name of what sortType's time is being displayed
         sortTimeString = '%16s'%sortTypes[sortIndex] + ' '

         #Append the times revelant to that sortType
         for time in avgTimes:
            sortTimeString += '{:12.6f}'.format(float(time))

         #Print the sortType times and loop again for every other sortType
         print(sortTimeString) 
         sortIndex +=1

      #Extra prints for formatting
      print()
      print()

main()
                                   

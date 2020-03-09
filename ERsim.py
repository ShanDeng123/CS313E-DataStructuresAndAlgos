#  File: ERsim.py
#  Description: HW5 - Creating queues to deal with ER priorities
#  Student's Name: Shan Deng
#  Student's UT EID: SD33857
#  Course Name: CS 313E 
#  Unique Number: 50739
#
#  Date Created: 3/12/19
#  Date Last Modified: 3/12/19

#Creation of a Queue class as given by Dr. Bulko
class Queue:

    #All Queues must also have a name
    def __init__(self,name):
        self.items = []
        self.name = name

    #If printed, return the name of the Queue
    def __str__(self):
        return self.name

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

#Adds a name to the given queue
def add(name,queue):
    queue.enqueue(name)
    print("--> Add patient " + name + " to " + str(queue) + " queue")
    print()

#Removes a name from the given queue through FIFO
def treat(queue):
    #Prints out the name that's being removed, and from which queue it's being removed from
    print("Treating " + queue.items.pop() + " from " + str(queue) +  " queue")


def main():

    #Initializing the 3 queues of different priorities
    c = Queue("Critical")
    s = Queue("Serious")
    f = Queue("Fair")

    #Reads from the given ERsim text file
    with open("ERsim.txt", "r") as testFile:

        #Loops through each line/command in the testfile
        for command in testFile:

            #Sets a boolean to only print a summary of Queue statuses if a successful change was made
            printStuff = True

            #If the line is a command to exit, stop reading from the file and end the program
            if command == "exit":
                print("--> Exit")
                break

            #If the line is a command to add
            elif "add" in command:
                #Split the line - spaces separate different details about what to add where
                details = command.split()

                #The third string of text is the destination Queue;
                #The second string of text is the name to be added
                #Checks for which queue to use; adds the given name to that queue
                if details[2] == "Critical":
                    add(details[1], c)
                elif details[2] == "Serious":
                    add(details[1], s)
                elif details[2] == "Fair":
                    add(details[1], f)

            #If the line isn't to add, but has a Queue name- it's always a treat() command
            #Checks which Queue is asked to be treated & re-prints the given command
            elif "Critical" in command:
                print("--> Treat next patient on Critical queue")
                print()

                #Checks if the given Queue is empty - Treats patients if there are any; If not print that there are no patients in the Queue
                if c.isEmpty():
                    print("No patients in queue")
                    printStuff = False
                else:
                    treat(c)

            #Same process as for treating Critical patients
            elif "Serious" in command:
                print("--> Treat next patient on Serious queue")
                print()
                if s.isEmpty():
                    print("No patients in queue")
                    printStuff = False
                else:
                    treat(s)

            #Same process as for treating Critical patients
            elif "Fair" in command:
                print("--> Treat next patient on Fair queue")
                print()
                if f.isEmpty():
                    print("No patients in queue")
                    printStuff = False
                else:
                    treat(f)

            #Checks each Queue by priority to treat the next given patient        
            elif "next" in command:
                print("--> Treat next patient")
                print()
                if c.isEmpty():
                    if s.isEmpty():
                        if f.isEmpty():
                            #If all queues are empty then print the "No Patients" error
                            print("No patients in queue")
                            printStuff = False
                        else:
                            treat(f)
                    else:
                        treat(s)
                else:
                    treat(c)

            #If the command is to treat all of the patients...
            elif "all" in command:
                print("--> Treat all patients")
                print()

                #Loops through each Queue by priority until they're all empty, and prints a summary after each loop
                while not(c.isEmpty() and s.isEmpty() and f.isEmpty()):
                    if c.isEmpty():
                        if s.isEmpty():
                            treat(f)
                        else:
                            treat(s)
                    else:
                        treat(c)
                    print("Queues are:")
                    print("Fair:     " + str(f.items))
                    print("Serious:  " + str(s.items))
                    print("Critical: " + str(c.items))
                    print()

                #When they're all empty, print out that there are no more patients in the Queue
                print("No patients in queue")
                #Don't print another summary after the end of the loop
                printStuff = False
                            
            #If an edit has been made and a summary output is needed...
            if printStuff:
                print("Queues are:")
                print("Fair:     " + str(f.items))
                print("Serious:  " + str(s.items))
                print("Critical: " + str(c.items))

            #Extra print call for cleaner formatting
            print()

#Runs the main
main()

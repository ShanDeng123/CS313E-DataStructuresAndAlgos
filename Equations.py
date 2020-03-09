#  File: Equations.py
#  Description: HW1 - Creating classes to compile Linear and Quadratic Equations
#  Student's Name: Shan Deng
#  Student's UT EID: SD33857
#  Course Name: CS 313E 
#  Unique Number: 50739
#
#  Date Created: 2/3/19
#  Date Last Modified: 2/3/19

class LinearEquation:

    #All linear equations will be in the form: y= (m)x + (b)
    def __init__(self,m,b):
        self.slope = m
        self.yintercept = b
        
    #When equations are printed, they will be simplified
    #
    def __str__(self):

        #If all values are 0, print 0
        if (self.slope == 0 and self.yintercept == 0):
            return "0"

        #If the slope is 0, just print the Y-Int value without add/sub symbols
        elif self.slope == 0:
            if self.yintercept < 0:
                return "- " + str(abs(self.yintercept))
            else:
                return str(self.yintercept)

        #Else, build the equation
        else:

            #Initialize base string
            outstr = ""

            #Writes first term of the equation
            #If the value is (-)1, do not print the coefficient
            #If the value is 0, skip printing the entire term (Checked above already)
            if (self.slope == 1):
                outstr += "x "
            elif (self.slope == -1):
                outstr += "- x "
            elif (self.slope < 0):
                outstr += "- " + str(abs(self.slope)) + "x "
            else:
                outstr += str(self.slope) + "x " 

            #Writes the constant of the equation
            #If the value is 0, skip printing the entire term
            #If the value is negative, use a subtraction sign
            if (self.yintercept == 0):
                pass
            elif (self.yintercept < 0):
                outstr += "- " + str(abs(self.yintercept))
                 
            else:
                outstr += "+ " + str(self.yintercept)

            #Returns the final equation
            return outstr

    def evaluate(self,x):
        return str(self.slope*x + self.yintercept)

    def __add__(self,otherLE):
        #Calculates using f(y) + f(z) = (a+c)x + (b+d) 
        newSlope = self.slope + otherLE.slope
        newYintercept = self.yintercept + otherLE.yintercept

        #Returns f(y) + f(z) as new LINEAR equation
        return LinearEquation(newSlope,newYintercept)

    def __sub__(self,otherLE):
        #Calculates using f(y) - f(z) = (a-c)x + (b-d) 
        newSlope = self.slope - otherLE.slope
        newYintercept = self.yintercept - otherLE.yintercept
        
        #Returns f(y) - f(z) as new LINEAR equation
        return LinearEquation(newSlope,newYintercept)

    def __mul__(self,otherLE):
        #Calculates using f(y) * f(z) = (ac)x^2 + (ad+bc)x + (bd) 
        newQuad = self.slope * otherLE.slope
        newSlope = (self.slope * otherLE.yintercept) + (otherLE.slope * self.yintercept)
        newYintercept = self.yintercept * otherLE.yintercept

        #Returns f(y) - f(z) as new QUADRATIC equation
        return QuadraticEquation(newQuad,newSlope,newYintercept)

    def compose(self,otherLE):
        #Calculates f(y(z)); self is f(y), otherLE is f(z)
        newSlope = self.slope * otherLE.slope
        newYintercept = (self.slope * otherLE.yintercept) + self.yintercept

        #Returns f(y(z)) as new LINEAR equation
        return LinearEquation(newSlope,newYintercept)


class QuadraticEquation:

    #All quadratic equations will be in the form: y= (a)x^2 + (b)x + c
    def __init__(self,a,b,c):
        self.quad = a
        self.slope = b
        self.yintercept = c
        
    def __str__(self):

        #If the quadratic has an a-value of 0, simplify it like a linear equation
        if (self.quad == 0):
            print(LinearEquation(b,c))
        
        else:
            
            #initialize base string
            outstr = ""

            #If the quadratic has a coefficient of (-)1, remove the "1"
            if (self.quad == 1):
                outstr += "x\u00B2 "
            elif (self.quad == -1):
                outstr += "- x\u00B2 "
                
            #Otherwise, add to base string
            elif (self.quad < 0):
                outstr += "- " + str(abs(self.quad)) + "x\u00B2 "
            else:
                outstr += str(self.quad) + "x\u00B2 "

            #Similar process for slope
            #Negative slopes will also need a minus sign
            #Zero slope will be ignored in forming the final equation
            if (self.slope == 1):
                outstr += "+ x "
            elif (self.slope == -1):
                outstr += "- x "
            elif (self.slope == 0):
                pass
            elif (self.slope < 0):
                outstr += "- " + str(abs(self.slope)) + "x "
            else:
                outstr += "+ " + str(self.slope) + "x " 

            #Same checks for Y-Int
            if (self.yintercept == 0):
                pass
            elif (self.yintercept < 0):
                outstr += "- " + str(abs(self.yintercept))
            else:
                outstr += "+ " + str(self.yintercept)

            #Returns the final equation string
            return outstr

    def evaluate(self,x):
        #Calculates using y = (a)x^2 + (b)x + c
        return self.quad * x**2 + self.slope*x + self.yintercept

    #Addition and subtraction of quadratic equations are just the sum/difference of the (a's + b's + c's)
    #Returns the new equation just like the linear add/sub functions
    def __add__(self,otherQE):
        newQuad = self.quad + otherQE.quad
        newSlope = self.slope + otherQE.slope
        newYintercept = self.yintercept + otherQE.yintercept
        return QuadraticEquation(newQuad,newSlope,newYintercept)

    def __sub__(self,otherQE):
        newQuad = self.quad - otherQE.quad
        newSlope = self.slope - otherQE.slope
        newYintercept = self.yintercept - otherQE.yintercept
        return QuadraticEquation(newQuad,newSlope,newYintercept)

#Code given by Dr. Bulko for Testing
def main():

   f = LinearEquation(5,3)
   print("f(x) =",f)
   print("f(3) =",f.evaluate(3),"\n")
         
   g = LinearEquation(-2,-6)
   print("g(x) =",g)
   print("g(-2) =",g.evaluate(-2),"\n")

   h = f + g
   print("h(x) = f(x) + g(x) =",h)
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f - g
   print("j(x) = f(x) - g(x) =",j)
   print("j(-4) =",j.evaluate(-4),"\n")

   k = f.compose(g)
   print("k(x) = f(g(x)) =",k,"\n")
   
   m = g.compose(f)
   print("m(x) = g(f(x)) =",m,"\n")

   n = f * g
   print("n(x) = f(x) * g(x) =",n,"\n")

   g = LinearEquation(5,-3)
   print("g(x) =",g)
   print("g(-2) =",g.evaluate(-2),"\n")
   
   h = f + g
   print("h(x) = f(x) + g(x) =",h)
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f - g
   print("j(x) = f(x) - g(x) =",j)
   print("j(-4) =",j.evaluate(-4),"\n")
   
   p = QuadraticEquation(1,1,-6)
   print("p(x) =",p)
   print("p(3) =",g.evaluate(3),"\n")
   
   q = QuadraticEquation(2,1,4)
   print("q(x) =",q)
   print("q(-3) =",q.evaluate(-3),"\n")
   
   r = p + q
   print("r(x) = p(x) + q(x) =",r)
   print("r(-2) =",r.evaluate(-2),"\n")

   s = p - q
   print("s(x) = p(x) - q(x) =",s)
   print("s(1) =",s.evaluate(1),"\n")
   
main()

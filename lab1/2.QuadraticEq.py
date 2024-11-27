#TASK: Make program that can work out Quadratic Equations

#------------------

#IMPORT MODULES
import math


#-------------

#SET FUNCTION
def solver():

    #SET VARIABLES 
    A=float(input("Enter A:"))
    B=float(input("Enter B:"))
    C=float(input("Enter C:"))
    
    #CALC QUADRATIC FORMULA
    root1=(-B+math.sqrt(B**2-4*A*C))/(2*A)
    print("This First Root is",root1)

    root2=(-B-math.sqrt(B**2-4*A*C))/(2*A)
    print("This Second Root is",root2)


solver()

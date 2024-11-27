#Implementation of BMI Program

#Calculates a person's BMI and Weight from User Input


name = input("What Is Your Name?")
weight = float(input("What Is Your Weight?"))
height = float(input("What Is Your Height in Meters?"))

BMI = weight/(height**2)

str_BMI = str(BMI)

print("Hello " + name + " your BMI is " + str_BMI)

class Calculator:
   







    
    # ----- PUBLIC Methods: That External Code can utilize) -----
    def Add(self):
            print("------ADDITION-------")
            num1 = int(input("Enter a Number"))
            num2 = int(input("Enter a Number"))
        
            result = num1 + num2
            print(result)

    def Subtract(self):
            num1 = int(input("Enter a Number"))
            num2 = int(input("Enter a Number"))

            result = num1 - num2

            print(result)

    def Multiply(self):
            num1 = int(input("Enter a Number"))
            num2 = int(input("Enter a Number"))

            result = num1*num2

            print(result)

    def Divide(self):
            num1 = int(input("Enter a Number"))
            num2 = int(input("Enter a Number"))

            result = num1/num2

            print(result)

    

    def Quit(self):
            quits = q



    #------ PRIVATE Methods; Not usable by external code ------
    def Show_Menu(self):
        
        input("Select an option:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\nq Quit")

        if input == "1":
            Calculator.Add()
        elif input == "2":
            Calculator.Subtract()
        elif input =="3":
            Calculator.Multiply()
        elif input == "4":
            Calculator.Divide()
        elif input == "q":
            Calculator.Divide()
        else:
            print("Invalid Option Selected")


 
calc=Calculator()

if __name__ == "__run_calculator__":
   calc.Show_Menu() 

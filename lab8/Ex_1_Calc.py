import tkinter 

class Calculator_GUI:
    def __init__(self, total):
        #pass the total parameter because it needs to be used by  addition,   minus   and reset functions
        self.mw = tkinter.Tk()
        
        self.total = 0      #sets initial total to 0
        self.total_label = tkinter.Label(self.mw, text="Total:")    #create label displaying total
        self.label_variable = tkinter.StringVar()   #create the variable allowing us to dynamically substitute in running total to display it
        self.label1 = tkinter.Label(self.mw, textvariable=self.label_variable) #Create the label that will actually DISPLAY the dynamic running total variable
        
        self.entry = tkinter.Entry(self.mw, width=15)  #create the entry field for the calculator user input
        
        self.plusbutton = tkinter.Button(self.mw, text="+", command=self.addition)   #create plus butto with callbacak to addition function
        self.minusbutton = tkinter.Button(self.mw, text="-", command=self.minus) #create subtraction button with callback to subtraction function

        self.reset = tkinter.Button(self.mw, text="Reset", command=self.Reset)  #create reset button with callback to reset function
        #position widgets
        self.total_label.grid(column=0, row=0)
        self.label1.grid(column=4, row=0)
        self.entry.grid(column=0, row=1)
        self.plusbutton.grid(column=1, row=2)
        self.minusbutton.grid(column=3, row=2)
        self.reset.grid(column=4, row=2)
        
        tkinter.mainloop()  #start the tkinter loop gui



    def addition(self):
        current_val = self.entry.get()  #store the current value that has been inputted
        #clear entry box
        self.entry.delete(0,tkinter.END)

        self.total = self.total + int(current_val)  #update the self.total  by adding on the   value just inputted
        
        self.label_variable.set(self.total)     #inputting the   new  self.total   value  into  where the dybamic label is placed

    def minus(self):         #function is the same thing execept it is for subtraction
       current_val = self.entry.get()
       #clear entry box
       self.entry.delete(0,tkinter.END)

       self.total = self.total - int(current_val)

       self.label_variable.set(self.total)
        
    
    def Reset(self):
        current_val = 0
        self.total = 0
        self.label_variable.set(self.total)

Calculator_GUI(0)   #start the calcualtor GUI function setting the initial total to 0

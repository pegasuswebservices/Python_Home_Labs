import tkinter as tk



class WM266_Grade_Computation:
    def __init__(self):
        self.mw = tk.Tk()   #creates the root window
       
       #create name entry field and name label
        self.name_entry = tk.Entry(self.mw, width=15)
        self.name_label = tk.Label(self.mw, text="Name")

        self.name_entry.grid(column=1, row=0)
        self.name_label.grid(column=0, row=0)


        #create ID entry field and ID label
        self.id_entry = tk.Entry(self.mw, width=15)
        self.id_label = tk.Label(self.mw, text="Student ID")

        self.id_entry.grid(column=1, row=1)
        self.id_label.grid(column=0, row=1)

        #create WM266 Module Label 
        self.wm266_label = tk.Label(self.mw, text="WM266 Assessments")
        self.wm266_label.grid(column=0, row=2) 

        #Lab Submission Label and Entry
        self.lab_marks_label = tk.Label(self.mw, text="Lab Submission Marks:")
        self.lab_marks_entry = tk.Entry(self.mw, width=15)
        
        self.lab_marks_label.grid(column=0, row=3)
        self.lab_marks_entry.grid(column=1, row=3)

        #Quiz submission Label and Entry
        self.quiz_marks_label = tk.Label(self.mw, text="Quiz Marks:")
        self.quiz_marks_entry = tk.Entry(self.mw, width=15)

        self.quiz_marks_label.grid(column=0, row=4)
        self.quiz_marks_entry.grid(column=1, row=4)

        #Computer Program Label and Entry
        self.program_marks_label = tk.Label(self.mw, text="Computer Program Marks:")
        self.program_marks_entry = tk.Entry(self.mw, width=15)

        self.program_marks_label.grid(column=0, row=5)
        self.program_marks_entry.grid(column=1, row=5)

       #Submit Grade Button
        self.submit = tk.Button(self.mw, text="Submit Marks", command=self.submission)
        self.submit.grid(column=0, row=6)    

        tk.mainloop()

    def submission(self):   #create the grade submission function
        student_id = self.id_entry.get()
        name = self.name_entry.get()

        lab_marks = int(self.lab_marks_entry.get())
        quiz_marks = int(self.quiz_marks_entry.get())
        program_marks = int(self.program_marks_entry.get())

        #check if input score is above max for each assignment. If > max, set score to max for assignemtn. If not, get value from the input box

        if lab_marks > 30:
            lab_marks = 30
        
        if quiz_marks > 20:
            quiz_marks = 20

        if program_marks > 50:
            program_marks =50

        #totals up marks
        total_mark = lab_marks + quiz_marks + program_marks

        print(f'{student_id}\n{name}\n Lab Marks: {lab_marks}\n Quiz Marks: {quiz_marks}\n Computer Program Marks: {program_marks}\n Total Mark = {total_mark}/100 Your results have been saved to the file student_grades.txt')

        #Create and write to file
        student_grades_file = open('student_grades.txt','w')
        student_grades_file.write(f"Student ID Number: {student_id}\n Student Name: {name}\n Lab Marks: {lab_marks}/30\n Quiz Marks: {quiz_marks}/20\n Computer Program Marks: {program_marks}/50\n Total Mark = {total_mark}/100\n")

WM266_Grade_Computation()

#determine if employee is owed overtime

hours_worked = float(input("How many hours did you work this week?"))
wage = float(input("What is your hourly wage?"))
overtime_hours = hours_worked - 40
overtime_wage = (1.2*wage)*overtime_hours
str_overtime_wage = str(overtime_wage)
if hours_worked>40:
    print("You are owed an additional $" + str_overtime_wage) 
else:
    print("You are not entitled to overtime pay")

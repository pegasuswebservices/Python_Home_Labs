#Program to determine if LeapYear or not

Current_Year=int(input("What year is it?"))
if Current_Year % 4 ==0 and Current_Year % 100 != 0:
    print("Yes,", Current_Year, "is a Leap Year")
else:
    print("No,", Current_Year,"is not a Leap Year")

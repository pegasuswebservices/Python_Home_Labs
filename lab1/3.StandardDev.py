import math

num1=float(input("Enter The First Number:"))
num2=float(input("Enter The Second Number:"))
num3=float(input("Enter The Third Number:"))
num4=float(input("Enter The Fourth Number:"))
num5=float(input("Enter The Fifth Number:"))

def func():
    #sum
   total=num1+num2+num3+num4+num5
   print("total is:",total)

   #average
   average=total/5
   print("mean is:",average)

   #standard dev
   sigma=1/5*(((num1-average)**2)+((num2-average)**2)+((num3-average)**2)+((num4-average)**2)+((num5-average)**2))

   standard_dev=math.sqrt(sigma) #square roots the prev result to get the standard dev

   print("Standard Deviation is:",standard_dev)

func()






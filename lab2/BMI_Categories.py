name = input("What Is Your Name?")
weight = float(input("What Is Your Weight?"))
height = float(input("What Is Your Height in Meters?"))

BMI = weight/(height**2)

str_BMI = str(BMI)

print("Hello " + name + " your BMI is " + str_BMI, end='')

if BMI<18.5:
    print("Your BMI Category is Underweight")
elif 18.5<BMI<24.9:
    print("Your BMI Category is Healthy")
elif 25<BMI<29.9:
    print("Your BMI Category is Overweight")
else:
    print("Your BMI Category is Obese")

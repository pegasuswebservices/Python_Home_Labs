num = float(input("Enter a Number"))

if num/10 < 1:
    print(num, "is a 1 digit number")
elif num/100 <1 and num/10 >=1:
    print(num, "is a 2 digit number")
elif num/1000 <1 and num/100 >=1:
    print(num, "is a 3 digit number")
else:
    print(num, "is greater than a 3 digit number")

#See if number is palindrome

num = input("Enter a Number")
reverse = num[::-1]
if num == reverse:
    print("The Number is a palindrome")
else:
    print("The Number is not a Palindrome")

def main():
    list1=[]
    list2=[]
    input1 = int(input("Enter a number for first list "))
    input2  = int(input("Enter a number for second list "))
    while input1 != 999 or input2 !=999:
        list1.append(input1)
        list2.append(input2)
        if input1 == input2:
            print(input1, "is in both lists")
        elif input1 in list1 and input1 in list2 and input2 in list1 and input2 in list2:
            print(input1, "is in both lists and", input2, "is in both lists")
        
       
        elif input1 in list1 and input1 in list2 and input2 not in list1:
            print(input1, "is in both lists", input2, "is not in both lists")
        elif input2 in list1 and input2 in list2 and input1 not in list2:
            print(input2, "is in both lists", input1, "is not in both lists")
        else:
            print("The lists have no common numbers")
        print("Enter 999 to end the program, else enter another number")
        input1 = int(input("Enter a number for first list "))

        input2 = int(input("Enter a number for second list "))


if __name__ == "__main__":
    main()

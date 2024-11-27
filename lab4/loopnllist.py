friends = []

name = input("Enter a name of your friend ")

while name != "Quit":
    friends.append(name)
    friends.sort()
    print(friends)
    name = input("Enter a name of your friend ")


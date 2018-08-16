import math

x = int(input("Enter a number x: "))
y = int(input("Enter a number y: "))

print("(1) Show even numbers from x to y")
print("(2) Show odd numbers from x to y")
print("(3) Show the squares from x to y")
print("(4) Exit the program")

choice = input("Choose an option: ")

while choice != "4":
    if choice == "1":
        for i in range(x, y + 1):
            if i % 2 == 0:
                print(i, end=" ")
        print()
    elif choice == "2":
        for i in range(x, y + 1):
            if i % 2 != 0:
                print(i, end=" ")
        print()
    elif choice == "3":
        for i in range(x, y + 1):
            square = math.sqrt(i)
            number = len(str(square))
            if number == 3:
                print(i, end=" ")
        print()
    else:
        print("Invalid menu choice")

    print("(1) Show even numbers from x to y")
    print("(2) Show odd numbers from x to y")
    print("(3) Show the squares from x to y")
    print("(4) Exit the program")

    choice = input("Choose an option: ")

print("Program ended.")

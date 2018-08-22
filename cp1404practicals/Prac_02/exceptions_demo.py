"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError will occur when the input is not an integer
2. When will a ZeroDivisionError occur?
    A ZeroDivisionError will occur when the input for the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes.
"""

finished = False

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while not finished:
        if denominator == 0:
            print("Invalid denominator")
            denominator = int(input("Enter the denominator: "))
        else:
            finished = True
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

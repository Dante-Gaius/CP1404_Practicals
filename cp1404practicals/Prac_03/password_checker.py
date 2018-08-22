"""Dante Gaius"""


def main():
    password = get_password()
    asterisks(password)


def asterisks(password):
    for char in password:
        print("*", end="")


def get_password():
    password = input("Enter password:")
    while len(password) < 6:
        print("Invalid Password")
        password = input("Enter password")
    return password


main()

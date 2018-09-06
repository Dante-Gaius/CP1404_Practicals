strings = []
string = str(input("Enter string: "))
strings.append(string)
while string != "":
    string = str(input("Enter string: "))
    strings.append(string)

if len(set(strings)) == len(strings):
    print("No repeated strings entered")
else:
    print("Strings repeated")

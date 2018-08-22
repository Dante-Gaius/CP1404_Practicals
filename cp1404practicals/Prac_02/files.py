username = input("Enter name:")
out_file = "{}.txt".format(username)
file = open(out_file, 'w')
print("Your name is {}".format(username), file=file)
file.close()

in_file = open('numbers.txt', 'r')
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
print(number_1 + number_2)
in_file.close()

in_file = open('numbers.txt', 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)

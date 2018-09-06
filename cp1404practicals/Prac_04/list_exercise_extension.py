numbers = []
count = 1
number = int(input("Number {}:".format(count)))
numbers.append(number)
while number > 0:
    count += 1
    number = int(input("Number {}:".format(count)))
    numbers.append(number)

print("The first number is : {}".format(numbers[0]))
print("The last number is: {}". format(numbers[-1]))
print("The smallest number is: {}".format(min(numbers)))
print("The largest number is: {}".format(max(numbers)))
average_of_numbers = sum(numbers) / len(numbers)
print("The average of the numbers is: {}".format(average_of_numbers))

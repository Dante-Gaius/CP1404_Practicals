items = int(input("Number of Items: "))

while items < 0:
    print("invalid number of items")
    items = int(input("Number Of Items: "))

total = 0
for i in range(items):
    price = float(input("Price of items:"))
    total += price

print("Total price of {} items is $ {:.2f}".format(items, total))



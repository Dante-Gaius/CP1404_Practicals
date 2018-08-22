number_of_items = int(input("Number of items:"))

finished = False
while not finished:
    if number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items:"))
    else:
        finished = True
total_price = 0
for item in range(1, number_of_items + 1):
    price_of_item = float(input("Price of item: $"))
    total_price = total_price + price_of_item

print("Total price for {} items is: ${:.2f}".format(number_of_items, total_price))

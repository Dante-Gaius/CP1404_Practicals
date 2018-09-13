from guitar_class import Guitar

print("My Guitars!")

guitars = []
name = input("Name:")

while name != "":
    year = int(input("Year:"))
    cost = float(input("Cost:"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print()
    name = input("Name:")


name_length = max(len(guitar.name) for guitar in guitars)
cost_length = max(len(str(guitar.cost)) for guitar in guitars)

print()
print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = "(Vintage)" if guitar.is_vintage() else ""
    print("Guitar {}: {:{}} ({}), worth ${:.2f}{}".format(i, guitar.name, name_length,  guitar.year, guitar.cost,
                                                          vintage_string))

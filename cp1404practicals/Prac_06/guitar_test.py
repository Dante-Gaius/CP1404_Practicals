from guitar_class import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2012, 10245.60)
guitar1_age = guitar1.get_age()
guitar2_age = guitar2.get_age()
guitar1_status = guitar1.is_vintage()
guitar2_status = guitar2.is_vintage()

print('My Guitars!')
print(guitar1)
print('This guitar is {}years old'.format(guitar1_age))
if guitar1_status:
    print('This is a vintage guitar')
else:
    print('This is not a vintage guitar')

print()
print(guitar2)
print('This guitar is {}years old'.format(guitar2_age))
if guitar2_status:
    print('This is a vintage guitar')
else:
    print('This is not a vintage guitar')

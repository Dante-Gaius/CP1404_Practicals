from cp1404practicals.Prac_08.unreliable_car import UnreliableCar

for i in range(1, 11):
    my_car = UnreliableCar("My_car", 100, 10.2)
    print(my_car.drive(10))

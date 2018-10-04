from cp1404practicals.Prac_08.taxi import Taxi
from cp1404practicals.Prac_08.silver_taxi_service import SilverTaxiService


def main():
    taxis = [Taxi("Prius", 100), SilverTaxiService("Limo", 100, 2), SilverTaxiService("Hummer", 200, 4)]
    print("Let's Drive! \nQ - Quit \nC - Choose Taxi \nD - Drive")
    current_taxi = None
    bill = 0.0

    user_choice = input(">>> ").upper()
    while user_choice != "Q":
        if user_choice == "C":
            print("Taxis available \n0 - {} \n1 - {} \n2 - {}".format(taxis[0], taxis[1], taxis[2]))
            taxi_choice = int(input("Choose taxi: "))
            while taxi_choice > 2:
                print("Invalid Taxi choice \nChoose a valid taxi:")
                print("Taxis available \n0 - {} \n1 - {} \n2 - {}".format(taxis[0], taxis[1], taxis[2]))
                taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif user_choice == "D":
            if current_taxi is None:
                print("You must choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                drive_distance = int(input("Drive how far? "))
                current_taxi.drive(drive_distance)
                bill += current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.car_name, current_taxi.get_fare()))
        else:
            print("Invalid Menu choice \nChoose a valid menu option")

        print("Bill to date: ${:.2f}".format(bill))

        print("Q - Quit \nC - Choose Taxi \nD - Drive")
        user_choice = input(">>> ").upper()

    print("Total trip cost: ${:.2f}".format(bill))
    print("Taxis are now: \n0 - {} \n 1 - {} \n 2 - {}".format(taxis[0], taxis[1], taxis[2]))


main()

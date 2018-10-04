from cp1404practicals.Prac_08.silver_taxi_service import SilverTaxiService

hummer = SilverTaxiService("Hummer", 200, 2)
hummer.drive(18)
fare = hummer.get_fare()
print(hummer)
print("Taxi fare = ${:.2f}".format(fare))

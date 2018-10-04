from cp1404practicals.Prac_08.taxi import Taxi

prius_1 = Taxi("Prius 1", 100)
prius_1.drive(40)
print(prius_1)
print("Current fare =", prius_1.get_fare())
print()

prius_1.start_fare()
print(prius_1)
print("Current fare =", prius_1.get_fare())
print()

prius_1.drive(100)
print(prius_1)
print(prius_1.get_fare())

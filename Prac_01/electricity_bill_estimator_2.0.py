TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff = input("Which tariff? 11 or 31: ")

daily_use = float(input("Enter daily use in KWh: "))
days = int(input("Enter number of billing days: "))

if tariff == "11":
    bill = days * daily_use * TARIFF_11
else:
    bill = days * daily_use * TARIFF_31

print("Estimated bill: ${:.2f}".format(bill))

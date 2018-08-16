price = float(input("Enter cents per KWh: "))
daily_use = float(input("Enter daily use in KWh: "))
days = int(input("Enter number of billing days: "))

bill = (price / 100) * daily_use * days

print("Estimated bill: $ {:.2f}".format(bill))

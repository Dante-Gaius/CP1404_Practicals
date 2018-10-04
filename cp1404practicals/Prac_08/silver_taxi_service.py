from cp1404practicals.Prac_08.taxi import Taxi


class SilverTaxiService(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = fanciness * Taxi.price_per_km

    def get_fare(self):
        new_fare = super().get_fare()
        return new_fare + self.flagfall

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

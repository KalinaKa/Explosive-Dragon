class Device(object):

    def __init__(self, name, power):
        """
        type: zelazko, czajnik elektryczny,
        kuchnia mikrofalowa, toster, odkurzacz

        """
        self.name = name
        self.power = power
        self.standby = True
        self.eco = True

    def power_consumption(self):
        if self.power <= 1000:
            print("Niskie zużycie energii.")
        elif self.power > 1000 and self.power <= 2000:
            print("Umiarkowane zużycie energii.")
        else:
            print("Wysokie zużycie energii")

    def yearly_consumption_price(self, time, price = 0.5):
        cost = (self.power * time) * price
        return cost

    def turn_on(self):
        self.standby = False
        if self.name.endswith('a') or self.name.endswith('o'):
            print(f"{self.name} zostało włączone.")
        else:
            print(f"{self.name} został włączony.")

    def __str__(self):
        return f"{self.name.capitalize()} to urządzenie gospodarstwa domowego."
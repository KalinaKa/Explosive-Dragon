class Fruit(object):

    def __init__(self, sort, shape, weight):
        self.sort = sort
        self.shape = shape
        self.weight = weight
        self.clean = False
        self.price = None

    def buy_units(self, units):
        if units == 1:
            print(f'Can I have just one {units} {self.sort}, please?')
        if units > 1:
            print(f'Can I have {units} units of {self.sort}, please?')

    def cost(self):
        if self.price >= 10:
            print("It's expensive")
        if self.price >= 4 and self.price <10:
            print("It's not cheap, but you can afford")
        else:
            print("It's cheap, buy plenty!")

    def wash_it(self):
        self.clean = True


    def __str__(self):
        print(f'This fruit is called {self.sort}.')
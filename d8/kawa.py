'''
zapytaj sie o printowanie intów.
jak definiowac mozliwe do wpisania wartosci i je walidowac w polu?
'''
class Coffee(object):

    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price
        self.togo = False


    def coffee_to_go(self):
        self.togo = True
        print('Coffee to go')

    def sell_coffee(self):
        how_much_coffee = input('How many coffies do you want?\n')
        quantity = int(how_much_coffee)
        price = quantity * self.price
        print(f'You pay {str(price)} PLN.')

    def __str__(self):
        print(f'This is {self.name}, size {self.size}.')

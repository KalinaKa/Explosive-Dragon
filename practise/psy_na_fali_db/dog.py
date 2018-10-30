class Dog(object):
    counter = 0

    def __init__(self, call_name, pedigree_name, breed, age, handler, ob_class):
        self.call_name = call_name
        self.pedigree_name = pedigree_name
        self.breed = breed
        self.__age = age
        self.handler = handler
        self.__ob_class = ob_class
        Dog.counter += 1

    @property
    def age(self):
        if self.__age is None:
            return 0
        else:
            self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self.__age = value

    @property
    def ob_class(self):
        if self.__ob_class is None:
            return 0
        else:
            self.__ob_class

    @ob_class.setter
    def ob_class(self, value):
        if isinstance(value, int):
            self.__ob_class = value

    #def __del__(self):
        #Dog.counter -= 1
        #print(f'Pies: {self.pedigree_name} został usunięty z bazy.')


    def __str__(self):
        print(f'{self.pedigree_name}, rasy {self.breed}, lat {str(self.age)}, handler {self.handler}, '
              f'klasa obedience: {str(self.ob_class)}.')


if __name__ == "__main__":
    Smok = Dog('Smok', 'Delayla Explosive Burst', 'Toller', 4, 'Ania', 2)
    print(Smok)
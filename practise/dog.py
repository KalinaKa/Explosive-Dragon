class Dog(object):
    counter = 0

    def __init__(self, call_name, breed, age, sex, handler, ob_class):
        self.call_name = call_name
        self.breed = breed
        self.__age = age
        self.sex = sex
        self.handler = handler
        self.__ob_class = ob_class
        Dog.counter += 1

    @property
    def age(self):
        if self.__age is None:
            return 0
        else:
            return self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self.__age = value

    @property
    def ob_class(self):
        if self.__ob_class is None:
            return 0
        else:
            return self.__ob_class

    @ob_class.setter
    def ob_class(self, value):
        if isinstance(value, int):
            self.__ob_class = value

    def serialiaze(self):
        new_dog = dict(call_name=self.call_name, breed=self.breed, age=self.age, sex=self.sex, handler=self.handler)
        return new_dog


    def __str__(self):
        return(f'{self.call_name} - {self.sex}, rasy {self.breed}, lat {str(self.age)}, handler {self.handler}, '
              f'klasa obedience: {str(self.ob_class)}.')


if __name__ == "__main__":
    Smok = Dog('Smok', 'Toller', 4, 'M', 'Ania', 2)
    new_dog = Smok.serialiaze()
    print(new_dog)
    print(Dog.counter)
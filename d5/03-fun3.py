# -*- coding: utf-8 -*-
# Mnożenie przy wypisywaniu.

def hello(name, age):
    print("{} is {} months old.".format(name.capitalize(), 12 * age))


hello("anna", 28)
hello("anna", "twenty")

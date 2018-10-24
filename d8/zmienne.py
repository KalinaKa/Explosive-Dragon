'''
globalne:
tu nie trzeba zwracac wartosci w return
tu zmieniliśmy coś na obiekcie globalnym
'''

imie = 'Ola'

def zmien_imie():
    global imie
    imie = 'Ala'

zmien_imie()
print(imie)
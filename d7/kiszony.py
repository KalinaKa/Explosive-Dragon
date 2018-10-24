import pickle

baza = [{'id': 1, 'imie':'Jan', 'dzieci':['ola', 'ala']},
        {'id': 2, 'imie': 'Janina', 'dzieci': ['ala']}
        ]
'''
dump zamienia na bajty,
zapisuje do pliku

dumps - string
'''

with open('baza.pickle', 'wb') as file:
    pickle.dump(baza, file)
    kisz = pickle.dumps(baza)

    print(kisz)

#Może też być pusta baza. Konwencja None też super.
baza_odczytana = None

with open('baza.pickle', 'rb') as file:
    baza_odczytana = pickle.load(file)

print(baza_odczytana)
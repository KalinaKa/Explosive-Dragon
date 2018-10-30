import pickle
from practise.psy_na_fali_db.dog import Dog

'''
funkcja czyszcząca input
'''
def clean_phrase(phrase):
    phrase = phrase.strip().capitalize()
    return phrase

'''
Pusta lista, do której będą appendowane nowe psy.
Będzie zapisywana do bazy.
'''
db = []

'''
Testowa pętla sprawdzająca funkcjonalność dodawania psa w oparciu o tworzenie kolejnych instancji klasy Dog
'''

for i in range(3):
    # dodawanie psa do bazy
    dog_name = input('Wpisz imię domowe psa:\n')
    dog_name = clean_phrase(dog_name)

    pedigree_name = input('Wpisz imię rodowodowe psa:\n')
    pedigree_name = clean_phrase(pedigree_name)

    breed = input('Wpisz rasę psa (bez skrótów):\n')
    breed = clean_phrase(breed)

    age = input('Podaj wiek psa w latach:\n')
    age = int(age)

    handler = input('Podaj imię przewodnika psa:\n')
    handler = clean_phrase(handler)

    ob_class = input('Podaj klasę obedience:\n')
    ob_class = int(ob_class)

    '''
    Tworzenie obiektu
    '''
    r = Dog(dog_name, pedigree_name, breed, age, handler, ob_class)
    r.ob_class = ob_class
    r.age = age

    '''
    baza oraz slownik tworzony polami instancji klasy Dog
    nie działa nadpisywanie zmiennych prywatnych via setter -,-
    '''

    row = {'id': r.counter,'imię': r.call_name, 'imię rodowodowe': r.pedigree_name, 'rasa': r.breed, 'wiek': r.age,
           'handler': r.handler, 'kl_obi': r.ob_class}
    db.append(row)


print(db)


'''
Zapis listy z nowymi psami do bazy
'''
with open('baza.pickle', 'ab') as file:
    pickle.dump(db, file)
    kisz = pickle.dumps(db)
    print(kisz)

'''
Baza odczytana błędnie zwraca tylko pierwszy zapisany rekord
'''
baza_odczytana = None

with open('baza.pickle', 'rb') as file:
    baza_odczytana = pickle.load(file)

print(baza_odczytana)

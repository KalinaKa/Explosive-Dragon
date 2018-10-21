specify_action = input('Baza psów klubu sportowego "Na Fali."\n'
                       'Wybierz akcję spośród możliwych wariantów, wpisując odpowiadającą mu literę:\n'
                       'A: Dodaj psa\n'
                       'B: Zmień imię psa\n'
                       'C: Sprawdź ogólną liczbę psów w klubie\n'
                       'Q: Wyjdź z programu\n'
                       'Wybierz akcję:\n'
                       )
specify_action = specify_action.strip().upper()
'''
FUNKCJE:
'''

'''
1. Funkcja odczytująca bazę danych Psów Na Fali
'''
def create_temporary_db():
    dogs = []

    with open('psy_na_fali_db.csv', encoding='utf-8') as file:
        line = file.readline()

        while line != "":
            line = line.rstrip()
            dog = line.split(',')

            dog[1] = float(dog[1])
            dogs.append(dog)

            line = file.readline()
        return dogs

'''
2. Zapis do bazy danych, gdy User dodaje nowego psa.
'''
def baza_a(dog_name, age, breed, sex, handler):
    with open('psy_na_fali_db.csv', 'a', encoding='utf-8') as file:
        rekord = (dog_name + ',' + age + ',' + breed + ',' + sex + ',' + handler + '\n')
        file.write(rekord)

'''
3. Zwraca tekstowy rekord z listy list o nazwie DOGS, po tym jak User zedytuje imię psa.
'''
def record_to_append(list):

    for a in range(len(dogs)):
        dog_name = dogs[a][0]
        age = dogs[a][1]
        breed = dogs[a][2]
        sex = dogs[a][3]
        handler = dogs[a][4]
        rekord = dog_name + ',' + age + ',' + breed + ',' + sex + ',' + handler

        list.append(rekord + '\n')

'''
4. Zapis danych do bazy po edycji imienia psa.
'''
def baza_b(baza):
    with open('psy_na_fali_db.csv', 'w', encoding='utf-8') as file:
        file.writelines(baza)

'''
5. Funkcja zrwaca strymowane słowo pisane z dużej litery.
'''
def clean_phrase(phrase):
    phrase= phrase.strip().capitalize()
    return phrase

'''
Główny program
'''



if specify_action == 'A':
    dog_name = input('Wpisz imię domowe psa:\n')
    dog_name = clean_phrase(dog_name)

    age = input('Podaj wiek psa w latach:\n')

    breed = input('Wpisz rasę psa (bez skrótów):\n')
    breed = clean_phrase(breed)

    sex = input('Podaj płeć: F - suczka, M - samiec:\n')
    sex = clean_phrase(sex)

    handler = input('Podaj imię przewodnika psa:\n')
    handler = clean_phrase(handler)

    baza_a(dog_name, age, breed, sex, handler)

    print('Pies {}, lat {}, rasy {}, płci {}, którego przewodnikiem jest {}, został dodany do bazy.'.format(
        dog_name, age, breed, sex, handler
    ))

elif specify_action == 'B':

    name_to_edit = input('Podaj imię psa, którego chcesz edytować:\n')
    name_to_edit = clean_phrase(name_to_edit)

    dogs = create_temporary_db()
    dog_names = []

    for i in range(len(dogs)):
        dog_names.append(dogs[i][0])

    if name_to_edit in dog_names:
        new_name = input('Podaj nowe imię psa:\n')
        new_name = clean_phrase(new_name)

        for i in range(len(dogs)):
            if name_to_edit == dogs[i][0]:
                dogs[i][0] = new_name
                break

        for i in range(len(dogs)):
            dogs[i][1] = str(dogs[i][1])

        copy_dogs = []
        record_to_append(copy_dogs)
        baza_b(copy_dogs)

        print('Imię psa zostało zmienione na {}.'.format(new_name))

    else:
        print("Psa o podanym imieniu nie ma w bazie.\n Oto lista dostępnych psów:\n {}".format(dog_names))

elif specify_action == 'C':
    dogs = create_temporary_db()
    how_many_records = len(dogs)

    print('W bazie znajduje się aktualnie {} psów.'.format(how_many_records))

elif specify_action == 'Q':
    print('Dzięki za skorzystanie z bazy Psów Na Fali. Do następnego!')
    exit(0)

else:
    print('Nie rozumiem Twojej komendy. Podaj właściwą. :)')

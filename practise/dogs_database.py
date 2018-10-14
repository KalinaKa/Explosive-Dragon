'''
Niestety, nie wiem, jak usunąć imię, gdy typem danych jest lista list.
Próba poniżej:

elif specify_action == 'B':
    name_to_remove = input('Podaj imię psa, które chcesz usunąć:\n')
    name_to_remove = name_to_remove.strip().capitalize()

    dogs = create_temporary_db()

    if name_to_remove in dogs:
        dogs.remove(name_to_remove)
        print('Imię psa zostało usunięte z bazy.')
'''


specify_action = input('Baza psów klubu sportowego "Na Fali."\n'
                       'Wybierz akcję spośród możliwych wariantów, wpisując odpowiadającą mu literę:\n'
                       'A: Dodaj psa\n'
                       'B: (dostępne wkrótce) Usuń imię psa\n'
                       'C: Sprawdź ogólną liczbę psów w klubie\n'
                       'Q: Wyjdź z programu\n'
                       'Wybierz akcję:\n'
                       )
specify_action = specify_action.strip().upper()
#print(specify_action)



'''Funkcja odczytująca bazę danych'''

def create_temporary_db():
    dogs = []

    with open('psy_na_fali.csv', encoding='utf-8') as file:
        line = file.readline()

        while line != "":
            line = line.rstrip()
            dog = line.split(',')

            dog[1] = float(dog[1])
            dogs.append(dog)

            line = file.readline()
        return dogs



if specify_action == 'A':
    dog_name = input('Wpisz imię domowe psa:\n')
    dog_name = dog_name.strip().capitalize()

    age = input('Podaj wiek psa w latach:\n')

    breed = input('Wpisz rasę psa (bez skrótów):\n')
    breed=breed.strip().capitalize()

    sex = input('Podaj płeć: F - suczka, M - samiec:\n')
    sex = sex.strip().upper()

    handler = input('Podaj imię przewodnika psa:\n')
    handler = handler.strip().capitalize()


    with open('psy_na_fali.csv', 'a', encoding='utf-8') as file:
        rekord = (dog_name + ',' + age + ',' + breed + ',' + sex + ',' + handler + '\n')
        file.write(rekord)

    print('Pies {}, lat {}, rasy {}, płci {}, którego przewodnikiem jest {}, został dodany do bazy.'.format(
        dog_name, age, breed, sex, handler
    ))

elif specify_action == 'C':
    dogs = create_temporary_db()
    how_many_records = len(dogs)

    print('W bazie znajduje się aktualnie {} psów.'.format(how_many_records))

elif specify_action == 'Q':
    print('Dzięki za skorzystanie z bazy Psów Na Fali. Do następnego!')
    exit(0)

else:
    print('Nie rozumiem Twojej komendy. Podaj właściwą. :)')
from practise.psy_na_fali_db.dog import Dog
import json

def clean_phrase(phrase):
    """Czyści input usera"""
    phrase = phrase.strip().capitalize()
    return phrase

def import_db():
    """Importuje obecną bazę danych"""
    json_db = open('na_fali_db.csv', 'r', encoding='utf-8')
    db_reader = json.load(json_db)
    json_db.close()
    return db_reader

def add_dog():
    '''Dodaje nowego psa do bazy'''
    call_name = input('1: Podaj domowe IMIĘ psa:\n')
    while call_name.isalpha() == False:
        if call_name.isalpha():
            call_name = clean_phrase(call_name)
            print(call_name)
        else:
            call_name = input("""Imię nie może zawierać cyfr. 
            ---> Popraw imię psa.\n""")
            call_name = clean_phrase(call_name)

    breed = input('2: Podaj RASĘ psa (nie używaj skrótów):\n')
    breed = breed.strip().title()
    #print(breed)

    age = input('3: Podaj WIEK psa w latach:\n')
    while age.isdigit() == False:
        if age.isdigit() == False:
            age = input("""UWAGA: Wiek powinien składać się z liczb całkowitych.
                    ---> Podaj wiek w liczbach całkowitych.\n""")
        else:
            age = int(age)

    sex = input('4: Podaj PŁEĆ zwierzaka (M - pies, F - suka):\n')
    while (sex.isalpha() and len(sex) == 1) == False:
        if sex.isalpha() and len(sex) == 1:
            sex = clean_phrase(sex)
        else:
            sex = input("""Płeć zwierzaka powinna być wyrażona jedną literą:
            M - pies,
            F - suka.
            ---> Wpisz poprawną wartość.\n""")
            sex = clean_phrase(sex)

    handler = input('5: Podaj IMIĘ przewodnika psa:\n')
    handler = handler.strip().title()
    print(handler)

    ob_class = input('Podaj klasę obedience: 0, 1, 2 lub 3:\n')
    while ob_class.isdigit() == False:
        if ob_class.isdigit() == False:
            ob_class= input("""Klasa wyszkolenia obedience powinna być zapisana liczbą całkowitą: 0, 1, 2 lub 3. 
            ---> Popraw wartość.\n""")
        else:
            ob_class = int(ob_class)

    ''' Tworzenie nowego obiektu '''
    new_row = Dog(call_name, breed, age, sex,  handler, ob_class)
    print(f'Utworzono nowy rekord: {new_row}')

    ''' Serializacja nowego obiektu do słownika'''
    new_row= new_row.serialiaze()

    ''' Odczytanie obecnej bazy danych '''
    db_reader = import_db()
    #print(db_reader)

    '''Dodanie nowego rekordu do istniejącej bazy danych'''
    db_reader['dogs'].append(new_row)
    #print(db_reader)

    na_fali_db = open("na_fali_db.csv", 'w', encoding="utf-8")
    json.dump(db_reader, na_fali_db, ensure_ascii=False)
    na_fali_db.close()


def count_dogs():
    '''Zlicza psy obecne w bazie'''
    current_db = import_db()

    how_many_dogs = len(current_db['dogs'])
    print(f'Ogólna liczba psów w bazie: {how_many_dogs}')

def display_dogs():
    '''Wyświetla iminona psów obecnych w bazie'''
    current_db = import_db()

    current_dog_names = []
    for dog in current_db['dogs']:
        current_name = (dog['call_name'])
        current_dog_names.append(current_name)
    print(f'Aktualnie w bazie znajdują się:\''
          f'{current_dog_names}')
import json

def clean_phrase(phrase):
    """Czyści input usera"""
    phrase = phrase.strip().capitalize()
    return phrase


def import_db():
    """Importuje obecną bazę danych"""
    json_db = open('na_fali_db2.csv', 'r', encoding='utf-8')
    db_reader = json.load(json_db)
    json_db.close()
    return db_reader


current_db = import_db()
#print(type(current_db))
#print(current_db)

#print(type(current_db['dogs']))

current_dog_names = []
for dog in current_db['dogs']:
    current_name = (dog['call_name'])
    current_dog_names.append(current_name)
print(f'Aktualnie w bazie znajdują się:\''
      f'{current_dog_names}')


dog_to_edit = input('Podaj imię psa, którego chcesz edytować:\n')
dog_to_edit = clean_phrase(dog_to_edit)

#znajduje imiona psów

if dog_to_edit in current_dog_names:
   edited_dog = dict()

   for dog in current_db['dogs']:
       call_name = dog['call_name']
       breed = dog['breed']
       age = dog['age']
       sex = dog['sex']
       handler = dog['handler']
       ob_class = dog['ob_class']

       #print(f'Imię: {call_name}')
       #print(f'Rasa: {breed}')
       #print(f'Wiek: {age}')
       #print(f'Płeć: {sex}')
       #print(f'Przewodnik: {handler}')
       #print(f'Klasa obedience: {ob_class}')

       edited_dog [call_name] = breed, age, sex, handler, ob_class

print(f'Pies wybrany do edycji to {dog_to_edit}.')
print('Obecne dane tego psa:')
print(edited_dog[dog_to_edit])

#dog_new_input = {"call_name" : None, "breed": None, "age" : None, "sex" : None, "handler" : None, "ob_class": None}

"""Zmienne pomocnicze: przechowują aktualne wartości edytowanego psa"""
current_call_name = dog_to_edit
current_breed = edited_dog[dog_to_edit][0]
current_age = edited_dog[dog_to_edit][1]
current_sex = edited_dog[dog_to_edit][2]
current_handler =  edited_dog[dog_to_edit][3]
current_ob_class = edited_dog[dog_to_edit][4]

"""
print('Aktualne dane:')
print(current_call_name)
print(current_breed)
print(current_age)
print(current_sex)
print(current_handler)
print(current_ob_class)
"""

edit_call_name = input('1: Czy chcesz zmienić domowe IMIĘ psa? [T / N]:\n')
edit_call_name = clean_phrase(edit_call_name)

if edit_call_name == 'T':
    new_call_name = input('Podaj nowe imię psa:\n')

    while new_call_name.isalpha() == False:
        if new_call_name.isalpha():
            new_call_name = clean_phrase(new_call_name)
            print(new_call_name)
        else:
            new_call_name = input("""Imię nie może zawierać cyfr. 
            ---> Popraw imię psa.\n""")
            new_call_name = clean_phrase(new_call_name)
            print(new_call_name)

else:
    new_call_name = current_call_name

dog_new_input = {"call_name" : new_call_name}
#print(f'Dane psa po zmianie {dog_new_input}')



edit_breed = input('2: Czy chcesz zmienić RASĘ psa? [T / N]:\n')
edit_breed = clean_phrase(edit_breed)
if edit_breed == 'T':
    new_breed = input('Podaj nową rasę psa:\n')
    new_breed = new_breed.strip().title()
else:
    new_breed = current_breed



edit_age = input('3: Czy chcesz zmienić WIEK psa? [T / N]:\n')
edit_age = clean_phrase(edit_age)

if edit_age == 'T':
    new_age = input('Podaj nowy WIEK psa w latach:\n')

    while new_age.isdigit() == False:
        if new_age.isdigit() == False:
            new_age = input("""UWAGA: Wiek powinien składać się z liczb całkowitych.
                    ---> Podaj wiek w liczbach całkowitych.\n""")
            print(new_age)
        else:
            new_age = int(age)
else:
    new_age = current_age

edit_sex = input('4: Czy chcesz zmienić PŁEĆ psa? [T / N]:\n')
edit_sex = clean_phrase(edit_sex)
if edit_sex == 'T':
    new_sex = input('Podaj nową PŁEĆ zwierzaka (M - pies, F - suka):\n')
    new_sex = new_sex.capitalize().strip()

    while (new_sex.isalpha() and len(new_sex) == 1) != True:
        new_sex = input("""Płeć zwierzaka powinna być wyrażona jedną literą:
        M - pies,
        F - suka.
        ---> Wpisz poprawną wartość.\n""")
        new_sex = new_sex.capitalize().strip()

else:
    new_sex = current_sex.strip().capitalize()
    print(new_sex)


edit_handler = input('5: Czy chesz edytować imię przewodnika? [T / N]:\n')
edit_handler = clean_phrase(edit_handler)
if edit_handler == 'T':
    new_handler = input('Podaj nowe IMIĘ przewodnika psa:\n')
    new_handler = new_handler.strip().title()
else:
    new_handler = current_handler


edit_ob_class = input('6: Czy chcesz zmienić KLASĘ obedience psa? [T / N]:\n')
edit_ob_class = clean_phrase(edit_ob_class)
if edit_ob_class == 'T':
    new_ob_class = input('Podaj nową klasę obedience: 0, 1, 2 lub 3:\n')
    while new_ob_class.isdigit() == False:
        if new_ob_class.isdigit() == False:
            new_ob_class= input("""Klasa wyszkolenia obedience powinna być zapisana liczbą całkowitą: 0, 1, 2 lub 3. 
            ---> Popraw wartość.\n""")
        else:
            new_ob_class = int(ob_class)
else:
    new_ob_class = current_ob_class



dog_new_input = {"call_name" : new_call_name, "breed": new_breed, "age" : new_age, "sex" : new_sex, "handler" : new_handler, "ob_class": new_ob_class}
print(f'Dane psa po zmianie {dog_new_input}')

'''
update
'''
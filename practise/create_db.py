import json


#Pierwszy input bazy
dogs = {"dogs":[{'call_name': 'Smok', 'breed': 'Toller', 'age': 4, 'sex': 'M', 'handler': 'Ania', 'class': 2},
{'call_name': 'Enox', 'breed': 'Owczarek Niemiecki', 'age': 4,'sex': 'M', 'handler': 'Ala', 'class': 2},
{'call_name': 'Zoom', 'breed': 'Border Collie', 'age': 6,'sex': 'M', 'handler': 'Magda', 'class': 3}]}

print(dogs)
print(len(dogs))

#JSON object
na_fali_db = open("na_fali_db.csv", 'w', encoding="utf-8")
json.dump(dogs, na_fali_db, ensure_ascii=False)
na_fali_db.close()
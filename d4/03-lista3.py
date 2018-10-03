# FIFO
# kolejka: pop wyciaga elementy o danym indeksie :) pop umozliwa wydobycie z listy i wpisanie do zmiennej
rzeczy = ["doniczka", "kwiatek", "ziemia", "woda"]

rzeczy.append("grabie")
element = rzeczy.pop(0)
print(element)
element = rzeczy.pop(0)
print(element)
element = rzeczy.pop(0)
print(element)
element = rzeczy.pop(0)
print(element)
element = rzeczy.pop(0)
print(element)
print("---------------\n")

# lifo - stos: zaprzeczenie kolejki, mamy dostep do tej wartosci co na gorze. pop bez indeksu bierze ost el z listy i daje do zmiennej.
rzeczy = ["doniczka", "kwiatek", "ziemia", "woda"]
rzeczy.append("łopata")
element = rzeczy.pop()
print(element)
element = rzeczy.pop()
print(element)
element = rzeczy.pop()
print(element)
element = rzeczy.pop()
print(element)
element = rzeczy.pop()
print(element)
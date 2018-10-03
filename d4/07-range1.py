#tu jest inaczej, bo pokazuje nam zakres ten print. aby to wypisac, nalezy go zamienic na liste.
#w pythonie 2 mozna bylo tak robic zakres, ale spowalnialo to procesor.
#w pythonie 3 to juz generator, generuje liczby na żądanie. dlatego wstepnie generuje "range(0,4)"
# wiec musimy skonwertowac do listy. w Pythonie 2 nazywano to xrange.

zakres = range(4)
print(zakres)
print(list(range(4)))


#lista
inty = [1, 2, 3, 4]
print(inty)


from d9.fauna import Zwierz
from d9.fauna import Czlowiek
from d9.fauna import Pies
from d9.fauna import Student


zwierz01 = Zwierz('pantofelek', 'bakterie')
zwierz02 = Zwierz('dżdżownica', 'bezkręgowce')

zwierz01.ruszaj()
zwierz02.ruszaj()

czlowiek01 = Czlowiek('Jan', 34)

"""
Od momentu, gdy zdefiniowano nową metodę ruszaj dla człowieka, nie szuka już w klasie zwierza
"""
czlowiek01.ruszaj()


print(type(czlowiek01))

pies01 = Pies('Smok', 'Toller')
print(type(pies01))
pies01.ruszaj()
pies01.bark()

pies02 = Pies('Berek', 'Golden')
print(pies02)
pies02.ruszaj()
pies02.bark()

student01 = Student('Gosia', 'politologia')
student01.ruszaj()
student01.powiedz('Panie Janie')
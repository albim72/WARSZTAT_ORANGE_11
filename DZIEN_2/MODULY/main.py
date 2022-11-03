import numpy
import sys
#import dane
#import dane as dn
from dane import nb,book
from mfunkcje_lib.bfunkcje import czytaj, czytaj_dict
from cls.sdane.czytaniedanych import CDane

print(nb)
print(book)
print(sys.path)

czytaj(nb)
czytaj_dict(book)

cd = CDane(nb,book)
print("_________________wypisanie za pomocą obiektu klasy CDane_______________________")

cd.czytaj_lista()
cd.czytaj_slow()

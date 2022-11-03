from osoba import Osoba
from trener import Trener

os1 = Osoba("Feliks",43,98,176)
os2 = Osoba()

os1.print_osoba()
os2.print_osoba()

print(os1.czyjesttrenerem())
print(os2.czyjesttrenerem())

print("__________________________________________")

tr1 = Trener("Jacek",40,77,178,4354,5,True,5,"Commando","ul.Złota 5 Kraków")

tr1.print_osoba()
print(tr1.opis_trenera())
print(f"czy osoba jest trenerem: {tr1.czyjesttrenerem()}")
tr1.klubinfo()


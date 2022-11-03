from osoba import Osoba
from trener import Trener
from klient import Klient

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

print("__________________________________________")

kl1 = Klient("Leon",40,80,180,678,"Lublin",nr_kb=7)

kl1.print_osoba()

print(kl1.czyjesttrenerem())


print("__________________________________________")

kl1 = Klient("Leon",40,80,180,678,"Lublin",nr_kb=7)

kl1.print_osoba()

print(kl1.czyjesttrenerem())

print("__________________________________________")

kl2 = Klient("Leon",40,80,180,678,"Lublin",54554,8,True,45,"Ole","CCC")

kl2.print_osoba()

print(kl2.czyjesttrenerem())

print(type(kl2.trener))



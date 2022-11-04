class MojWlasnySlownik(dict):

    def __missing__(self, key):
        return "uwaga! ten klucz nie istnieje."


slow = {'Alicja':45,"Eryk":88,"Nadia":80,"Miasto":"Kraków",1:2}

mojd = MojWlasnySlownik(slow)

print(mojd['Nadia'])
print(mojd['Henio'])
print(mojd['Miasto'])
print(mojd[1])
#print(slow['Henio'])
print(type(mojd))

nb = [5,8,2,1]
ml = MojWlasnySlownik(nb)

print(ml[1])

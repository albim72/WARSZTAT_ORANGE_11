from osoba import Osoba
from klub import Klub

class Trener(Osoba,Klub):
    
    def __init__(self,imie,wiek,waga,wzrost,nr_licencji,lata_dosw,expert,
                 nr_kb,nazwa_kb,adres_kb):
        Osoba.__init__(self,imie,wiek,waga,wzrost)
        Klub.__init__(self,nr_kb,nazwa_kb,adres_kb)
        self.expert = expert
        self.lata_dosw = lata_dosw
        self.nr_licencji = nr_licencji
        self.trener = True
        
    def opis_trenera(self):
        return f"Trener - > Licencja: {self.nr_licencji}, lata dośwadczenia: {self.lata_dosw}, " \
               f"poziom ekspercki? ({self.expert})"

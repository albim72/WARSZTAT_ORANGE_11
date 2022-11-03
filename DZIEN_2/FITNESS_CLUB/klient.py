from trener import Trener
from sport import Sport

class Klient(Trener,Sport):

    def __init__(self,imie,wiek,waga,wzrost,nr_klienta,miasto,nr_licencji="",lata_dosw="",expert="",
                 nr_kb="",nazwa_kb="",adres_kb="",dyscyplina="",lata_upr="",zyciowka=""):
        Trener.__init__(self,imie,wiek,waga,wzrost,nr_licencji,lata_dosw,expert,
                 nr_kb,nazwa_kb,adres_kb)
        Sport.__init__(self,dyscyplina,lata_upr,zyciowka)
        self.miasto = miasto
        self.nr_klienta = nr_klienta
        self.numerklienta()
        self.trener = None

    def numerklienta(self):
        print(f"przydzielono numer klienta: {self.nr_klienta}")

    def czyjesttrenerem(self):
        return self.nr_licencji != ""




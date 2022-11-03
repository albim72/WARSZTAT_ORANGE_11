class Osoba:
    
    def __init__(self,imie,wiek,waga,wzrost):
        self.wzrost = wzrost
        self.waga = waga
        self.wiek = wiek
        self.imie = imie
        self.koloroczu = "brązowe"
        self.trener = False
        
    def print_osoba(self):
        print(f"osoba -> {self.imie}, wiek: {self.wiek}, waga: {self.waga} kg, "
              f"wzrost: {self.wzrost} cm, kolor oczu: {self.koloroczu}")
        
    def czyjesttrenerem(self):
        return self.trener

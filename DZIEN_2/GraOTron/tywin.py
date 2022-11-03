from rod import CzlonekRodu

class Tywin(CzlonekRodu):

    def walka(self):
        if self.punkty_walki > self.punkty_palacowe:
            print(f"{self.tytul} wysłany do walki...")
        else:
            print(f"{self.tytul} pozostaje w pałacu....")

    def negocjacja(self):
        if self.punkty_palacowe >= 8 and self.punkty_walki<self.punkty_palacowe:
            print(f"{self.tytul} wysłany do negocjacji.....")
        else:
            print(f"{self.tytul} wysłany do walki")

    def uczta(self):
        pass

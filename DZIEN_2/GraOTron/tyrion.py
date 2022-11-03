from rod import CzlonekRodu

class Tyrion(CzlonekRodu):

    def walka(self):
        if self.punkty_walki > self.punkty_palacowe and self.punkty_walki>=6:
            print(f"{self.tytul} wysłany do walki...")
        else:
            print(f"{self.tytul} pozostaje w pałacu....")

    def negocjacja(self):
        if self.punkty_palacowe >= 8:
            print(f"{self.tytul} wysłany do negocjacji.....")
        else:
            print(f"{self.tytul} wysłany do walki")

    def uczta(self):
        if self.punkty_palacowe >= 6 and self.doswiadczenie >= 7:
            print(f"{self.tytul} jedzie na ucztę....")
        else:
            print(f"{self.tytul} pozostaje w pałacu....")

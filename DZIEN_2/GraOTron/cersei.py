from rod import CzlonekRodu

class Cersei(CzlonekRodu):

    def walka(self):
        if self.punkty_walki >=8:
            print(f"{self.tytul} udaje się na pole bitwy...")
        else:
            print(f"{self.tytul} pozostaje w pałacu....")

    def negocjacja(self):
        if self.punkty_palacowe >= 7:
            print(f"{self.tytul} wysłana do negocjacji.....")
        else:
            print(f"{self.tytul} wysłana do walki")

    def uczta(self):
        if self.punkty_palacowe >= 8 and self.doswiadczenie >= 8:
            print(f"{self.tytul} jedzie na ucztę....")
        else:
            print(f"{self.tytul} pozostaje w pałacu....")

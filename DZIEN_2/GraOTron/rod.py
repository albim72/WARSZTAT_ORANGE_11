from abc import ABC,abstractmethod

class CzlonekRodu(ABC):

    def __init__(self,nazwa_rodu,tytul,plec,punkty_walki,punkty_palacowe,doswiadczenie):
        self.doswiadczenie = doswiadczenie
        self.punkty_palacowe = punkty_palacowe
        self.punkty_walki = punkty_walki
        self.plec = plec
        self.tytul = tytul
        self.nazwa_rodu = nazwa_rodu

    def __repr__(self):
        return f"Ród: {self.nazwa_rodu}, tytuł -> {self.tytul} {self.__class__.__name__}"

    @abstractmethod
    def walka(self):
        pass

    @abstractmethod
    def negocjacja(self):
        pass

    @abstractmethod
    def uczta(self):
        pass




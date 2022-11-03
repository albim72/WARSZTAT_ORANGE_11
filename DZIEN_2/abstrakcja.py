import math
from abc import ABC, abstractmethod

class Figura(ABC):

    def __init__(self,a,b=0,c=0):
        self.a = a
        self.b = b
        self.c = c
        self.info()

    def info(self):
        return "tworzenie nowej figury..."

    @abstractmethod
    def wyznacz_czas(self):
        pass

    @abstractmethod
    def policz_pole(self):
        return self.a**2

class KwadratKolo(Figura):

    def wyznacz_czas(self):
        return 10

    def policz_pole(self):
        return super().policz_pole()+0.5*math.pi*self.a**2


kk = KwadratKolo(6)
print(kk.policz_pole())




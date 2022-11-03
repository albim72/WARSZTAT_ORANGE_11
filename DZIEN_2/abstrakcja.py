from abc import ABC, abstractmethod

class Figura(ABC):

    def __init__(self,a,b,c=0):
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

from mfunkcje_lib.bfunkcje import *

class CDane:
    
    def __init__(self,lista,dicts):
        self.lista = lista
        self.dicts = dicts
        
    def czytaj_lista(self):
        return czytaj(self.lista)
    
    def czytaj_slow(self):
        return czytaj_dict(self.dicts)
        

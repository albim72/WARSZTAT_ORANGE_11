class Sport:

    def __init__(self,dyscyplina,lata_upr,zyciowka):
        self.zyciowka = zyciowka
        self.lata_upr = lata_upr
        self.dyscyplina = dyscyplina
        self.dysc_przypisanie()
        
    def dysc_przypisanie(self):
        print(f"przypisanie do zajęć z dsycypliny: {self.dyscyplina}")
        
    def infosport(self):
        print(f"{self.dyscyplina}, lata uprawiania: {self.lata_upr}, rekord życiowy: {self.zyciowka}")

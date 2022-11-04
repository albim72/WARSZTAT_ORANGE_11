class Kolor:

    def __init__(self):
        print("Instancja klasy Kolor utworzona...")
        

    def __call__(self,info,nb):
        print(f"Instancja wołana przez specjalną metodę __call__ !!! - {info} {nb}")

gh = Kolor()

gh("takie tam",8.99)

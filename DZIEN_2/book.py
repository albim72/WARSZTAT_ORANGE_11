class Book:

    okladka_lakierowana = True
    #deklaracja stanu (dane) -> konstruktor klasy
    def __init__(self,id,tytul,autor,cena=10):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    #definicja zachowania
    def create_book(self):
        print("tworzenie nowej książki....")

    def print_book(self):
        print(f"książka {self.tytul}, autor: {self.autor}, cena: {self.cena} zł, "
              f"orawa: {self.oprawa}, czy okładka jest lakierowana? obiekt -> ({self.okladka_lakierowana}),"
              f"klasa -> {Book.okladka_lakierowana}")

    def rabat(self,procent):
        return (procent/100)*self.cena

    def get_tytul(self):
        return self.tytul

    def set_cena(self,nowacena):
        self.cena = nowacena



b1 = Book(35,"Wiedźmin","Andrzej Sapkowski",38)
b1.print_book()
print(f"rabat: {b1.rabat(7):.2f} zł")
print(f"cena do zapłaty: {b1.cena - b1.rabat(7)} zł")

print(b1.autor)
print(b1.get_tytul())

b1.set_cena(67)

b1.print_book()

#Book.okladka_lakierowana = False
b1.okladka_lakierowana = False

b1.print_book()

b2 = Book(67,"Hobbit","J.R.R. Tolkien",45)
b2.print_book()





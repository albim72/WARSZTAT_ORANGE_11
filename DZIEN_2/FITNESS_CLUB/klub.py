class Klub:

    def __init__(self,nr_kb,nazwa_kb,adres_kb):
        self.adres_kb = adres_kb
        self.nazwa_kb = nazwa_kb
        self.nr_kb = nr_kb
        self.przypisanie_kb()

    def przypisanie_kb(self):
        print(f"przypisanie do klubu: {self.nr_kb}")

    def klubinfo(self):
        print(f"klub {self.nazwa_kb}, adres: {self.adres_kb}")



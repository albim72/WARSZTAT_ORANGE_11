class Miasto:
    def __init__(self,trawnik):
        self.trawnik = trawnik

    def __getattr__(self, name):
        return f"Klasa Miasto nie posiada atrybutu: {name}"

hn = Miasto("trawnik")
print(hn.trawa)
print(hn.trawnik)

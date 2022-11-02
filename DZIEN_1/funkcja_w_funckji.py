def witaj(name):
    return f"Miło Cię znowu widzieć {name}"

def konkurs(imie,punkty):
    return f"uczestnik {imie}, liczba punktów: {punkty}"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Olga",67))

#przykład 2

def rejestracja(oplata):
    def lista():
        return "jesteś na liście zawodników"
    def brak():
        return "jeśli chcesz być na liście startowej, dokonaj wpłaty"
    def error():
        return "wpisz 1- wpłata, 0 - brak wpłaty"
    if oplata == 1:
        return lista
    elif oplata == 0:
        return brak
    else:
        return error

print(rejestracja(1)())
print(rejestracja(0)())
print(rejestracja(6)())

#funkcja wrapper

def startstop(funkcja):
    def wrapper(*args):
        print("startowanie procesu...")
        funkcja(*args)
        print("kończenie procesu.....")
    return wrapper


def zawijanie(czego):
    print(f"zawijanie {czego} w sreberka")

print("_________________________________")

zawijanie("ciastek")

zw = startstop(zawijanie)
zw("czekoladek")

#funkcja jawnie dekorująca
@startstop
def dmuchanie(co):
    print(f"dmuchanie {co} na imprezę...")


print("_________________________________")
dmuchanie("baloników")

print("_________________________________")

@startstop
def fn(n):
    print(f"wynik = {n*2-1}")

fn(19)


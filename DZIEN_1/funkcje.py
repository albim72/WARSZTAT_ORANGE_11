import math

#funkcja 1
n=4
m = 9
def policz(a,b,c,y):
    global n,m
    n = (a+b)*y-c + n - m
    return n

print(policz(3,6,8,2))
print(n)

#funkcja 2
x = 100
def zewnetrzna():
    #global x
    x = "lokalne"

    def wewnetrzna():
        nonlocal x
        #x=90
        print(f"wewnętrzne x = {x}")
    wewnetrzna()
    print(f"zewnętrzne x = {x}")

zewnetrzna()

#funkcja 3

def gx(n,m=1,k=3,b=5):
    return math.sqrt(n+m)*k-b

print(gx(3,6,8,1))
print(gx(3,6,8))
print(gx(3,6))
print(gx(3))

#wywołaj funkcję z wartościami n=9, m zostaw domyślną, k=11, b=2

print(gx(9,k=11,b=2))
print(gx(9,b=2,k=11))
#print(gx(b=2,9,k=11))

#funkcje anonimowe lambda:

print((lambda e:e**3)(5))

def ex(e):
    return e**3

print(ex(5))

s = lambda e,f=2:e-f
print(s(3,7))
print(s(3))


def ob(k):
    return lambda a,b:a**k-b

print(ob(5)(1,2))

def zw(k):
    return k

print((lambda a,b,k:a**zw(k)-b)(1,2,5))

num = [67,2,5,-177,34,122,4,7,1,100,-4,5,0]
#stwórz listę nparz i przekaż do niej wszystkie wartości parzyste z listy num
#użyj funkcji standardowej filter (funkcja wyższego rzędu -> gdzie parametr 0 funkcji to inna funkcja,
#paramet 1 to żródło danych)

nparz = list(filter(lambda x:x%2==0,num))
print(nparz)

#stwórz listę cube i przekaż do niej wszystkie wartości z listy num podniesione do potęgi 3

cube = list(map(lambda x:x**3,num))
print(cube)

def dodaj(x):
    return x + 33

trojka = list(map(dodaj,num))
print(trojka)

#własna funkcja wyższego rzędu

def filtrowanie(dane,test):

    plus = []
    for element in dane:
        if (test(element)):
            plus.append(element)
    return plus

def ekstra_liczba(n):
    return not n>=100

print(filtrowanie(num,ekstra_liczba))
print(filtrowanie(num,lambda x:x>=88))


def mapowanie(dane,transformacja,param):

    mapa=[]
    for element in dane:
        mapa.append(transformacja(element,param))
    return mapa

def addfive(n,m):
    return n+m

print(mapowanie(num,addfive,17))


import math
import time

def pomiarczasu(funkcja):

    def wrapper():
        starttime = time.perf_counter()
        print("uruchomienie funkcji....")
        funkcja()
        endtime=time.perf_counter()
        print(f"czas wykonania funkcji: {endtime - starttime} s")
    return wrapper


def sleep(funkcja):
    def wrapper():
        print("Włączenie sleep...")
        time.sleep(1)
        return funkcja()
    return wrapper

@sleep
@pomiarczasu
def biglista():
    sum([i**2 for i in range(1000000)])

biglista()
print("________________________________")
lt = [i**2 for i in range(1000000)]
@sleep
@pomiarczasu
def biglista_out():
    sum(lt)

biglista_out()

@sleep
@pomiarczasu
def biglista_math():
    sum([math.pow((i+1),6)+math.sqrt(i) for i in range(1000000)])

biglista_math()

#dekorator z funkcją magiczną __name__

def debug(funkcja):
    def wrapper(*args,**kwargs):
        print(f"wołana funkcja to: {funkcja.__name__}")
        funkcja(*args)
    return wrapper

@debug
def info(i):
    print(f"informacja: {i}")

info("nr 23534534534")


#repeater

def repeater(n):
    def wrapper(funkcja):
        def inner(*args):
            for i in range(n):
                funkcja(*args)
        return inner
    return wrapper

@repeater(n=7)
def komunikat(k,n):
    print(f'ważny komunikat: {k}, numer: {n}.')

komunikat("biało-czarne",9)

@repeater(n=8)
def hx(n):
    print((n-1)**7)

hx(11)


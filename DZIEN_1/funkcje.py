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


def liczby():
    for i in range(11):
        yield i*2

for p in liczby():
    print(p)

print(type(liczby()))

lu = list(liczby())
print(len(lu))


def wznowienie(n,k):
    print("wstrzymanie działania")
    yield 1008
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield 23400*n
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield 121390*k
    print("wznowienie działania")

for i in wznowienie(3,4):
    if i == 1008:
        continue
    print(f"wartość z yield: {i}")

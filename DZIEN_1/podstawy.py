print("to linia na dobry początek")

#komentarz zwykły
"""
komentarz dokuemntacyjny
wieloliniowy
"""

'''
to już nie jest komentarz dokumentacyjny
'''

imiona = ["Jan","Paweł","Leon","Anna","Olga","Leon","Tekla","Grzegorz","Magda","Leon"]

#CTRL+D - duplikacja linii/bloku
#CTRL + / - komentowanie/odkomentowanie bloku
print(imiona)
print(imiona[0])
print(imiona[1])
print(imiona[2:6])
print(imiona[-1])
print(imiona[-2])

w = "kalejdoskop"

print(w)
print(w[0])
print(w[1])

print(imiona[0][2])

imiona_p = imiona[::2] #[a:b:c], a,b, puste oznacza od początku do końca, c - krok

print(imiona_p)

imiona_np = imiona[1::2]

print(imiona_np)

wyr1 = "listopad"
wyr2 = "Urszula"

print(wyr1,":",wyr1[::-1])
print(wyr2,":",wyr2[::-1])

imiona.append("Klara")
print(imiona)

a="drużyna: \"Inter Mediolan\""

print(a)

imiona.insert(3,"Benedykt")
print(imiona)

im2 = imiona #to nie jest lista tylko referencja
im_p = imiona[:]
print(im_p)

im_q = list(imiona)
print(im_q)


k = 999
print(k)
print(type(k))

k = "dziewięć"
print(k)
print(type(k))

h:float #deklaracja typu
h = 9.67
print(h)
print(type(h))

h = True
print(h)
print(type(h))

h = ["blblblblb",534534,6.88,True]
print(h)
print(type(h))

h[0] = True

print(h)
print(type(h[0]),type(h[1]))


ndim = [[[[5,6,7,8]],[45,67,3,7,9]],[5,3,2,4,1]]

print(ndim[0])
print(ndim[0][0])
print(ndim[0][0][0][2])

#krotka

miasta = ("Kraków","Lublin","Warszawa","Kraków","Poznań")
print(miasta)
print(miasta[3])
print(miasta.count("Kraków"))
mn = miasta.index("Lublin")
print(miasta[mn])




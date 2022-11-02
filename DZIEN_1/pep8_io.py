marka = "Jeep"
model = "Cherokee"
rocznik = 2020

print("auto: "+marka+", model: "+model+", rocznik: "+str(rocznik))
print("marka:",marka,"model:",model,"rocznik:",rocznik,sep=" - ")

sam = "samochód -> marka: {}, model: {}, rocznik: {}."
print(sam.format(marka,model,rocznik))

sam = "samochód -> rocznik: {2}, marka: {0}, model: {1}."
print(sam.format(marka,model,rocznik))

#f-string

print(f"autokomis -> marka: {marka}, model: {model}, rocznik: {rocznik}")

konkurs = [
    ("Jan",78),
    ("Anna",45),
    ("Olaf",12),
    ("Olga",89),
    ("Leon",78),
    ("Nadia",67)
]

print("____________________________________________")
print(list(enumerate(konkurs)))

print("__________zestawienie wyników konkursu______________")

for i,(imie,punkty) in enumerate(konkurs):
    print('nr %d: %-9s : %.1f punktów' %(i+1,imie,punkty))

print("jestem poza pętlą...")

for i,(imie,punkty) in enumerate(konkurs):
    print(f'nr {i+1}: {imie:8s} : {punkty:.1f} punktów')

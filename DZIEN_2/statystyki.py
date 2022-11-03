import math

liczby = [56,1009,-876,1223,0,99,2,5,16,78,999,-100,8,677]

def statystyki(dane):
    minimum = min(dane)
    maksimum = max(dane)
    rozstep = maksimum - minimum
    liczba_el = len(dane)
    sr_arytm = sum(dane)/liczba_el
    suma_odchyl = sum(list(map(lambda x:x-sr_arytm,dane)))
    sr_odchyl_std = math.sqrt((suma_odchyl**2)/(liczba_el-1))
    return minimum,maksimum,rozstep,liczba_el,sr_arytm,sr_odchyl_std

wyniki = statystyki(liczby)
print(wyniki)
print(type(wyniki))

mini, maxi, roz, lb, sar, dev = statystyki(liczby)

opis = f"statystyki dla listy liczby:\n" \
       f"minimum: {mini}\n" \
       f"maximum: {maxi}\n" \
       f"rozstęp wartości: {roz}\n" \
       f"liczba elementów: {lb}\n" \
       f"średnia arytmetyczna: {sar}\n" \
       f"średnie odchylenie standardowe: {dev}."


print(opis)

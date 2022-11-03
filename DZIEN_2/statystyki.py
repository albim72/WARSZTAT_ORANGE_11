import math

liczby = [56,1009,-876,1223,0,99,2,5,16,78,999,-100,8,677]

def statystyki(dane):
    minimum = min(dane)
    maksimum = max(dane)
    liczba_el = len(dane)
    sr_arytm = sum(dane)/liczba_el
    suma_odchyl = sum(list(map(lambda x:x-sr_arytm,dane)))
    sr_odchyl_std = math.sqrt((suma_odchyl**2)/(liczba_el-1))
    return minimum,maksimum,liczba_el,sr_arytm,sr_odchyl_std

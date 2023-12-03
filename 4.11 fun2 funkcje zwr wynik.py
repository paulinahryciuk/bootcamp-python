def dodaj(a,b):
    return a+b
print(dodaj(6,9))

def oblicz_vat(cena, vat=23):
    return cena*(100+vat)/100

print(oblicz_vat((1000)))
print(oblicz_vat(1000,7))
print(oblicz_vat(vat = 8, cena = 1000))
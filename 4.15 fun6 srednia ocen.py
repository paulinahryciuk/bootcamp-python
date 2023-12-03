def srednia(*cyfry):
    print(cyfry)

srednia()
srednia(1)
srednia(1,2,3)

suma = 0
for c in cyfry:
    print(c)
    suma += c
count = len(cyfry)
print(f"srednia {suma/count}")

from decimal import Decimal

kwota1 = Decimal('10.25')
kwota2 = Decimal('5.50')
precyzja2 = Decimal('0.00')

suma = kwota1+kwota2
print(f"suma {suma}")

roznica = kwota1-kwota2
print(f"roznica {roznica}")
print(f"roznica {roznica.quantize((precyzja2))}")

# mnozenie
podatek = Decimal('0.23')
kw_z_pod = kwota1 * (1+podatek)
print(kw_z_pod)
print(kw_z_pod.quantize(precyzja2))

ilosc_osob = 3
rach_na_osob = kw_z_pod / ilosc_osob
print(rach_na_osob.quantize(precyzja2))
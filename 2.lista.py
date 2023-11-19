lista = []
print((lista))
print(type(lista))
print(bool(lista))

lista2 = [10,20,30]
print(lista2)

lista5 = [10.77, 30.66]
print(lista5)

lista4 = [10, 5.2, "oko"]
print(lista4)

print(len(lista4))


lista.append("A")
lista.append("B")
print(lista)
print(lista[0],lista[-2])
print(lista[1])
print(lista[-1])
print(lista[-2])

print(lista[0:1])
print(lista[:1])
print(lista[-2:])
print(lista[:])
print(lista[-1:0])

lista[1] = "CCC"
print(lista)
lista.insert(1,"YYY")
print(lista)

print(lista.pop(1))
print(lista)
ind = lista.index("A")
print(ind)
print(lista.pop(ind))
print(lista)

print(lista.remove("CCC"))
print(lista)

lista.append('ola')
lista.append('OLa')
lista.append('ania')
print("Ola" in lista)
print("ola" in lista)
print(lista)

liczby = [45, 999, 34, 22, 13.34,687]
print(liczby)
print(type(liczby))
liczby.sort()
print(liczby)

lista_osoby = [ 'radek', 'ola', 'agata', 'lena']
print(lista_osoby)
liczby = [45, 999, 34, 22, 13.34,687, 'A']

lista_osoby.sort(reverse= True)
print(lista_osoby)
print("#")
print(liczby)
elem = liczby[3]
liczby [3] = 10000
print(liczby)
print(liczby[-1])
print(liczby[(len(liczby))-1])
print(liczby)
liczby.pop(0)
liczby.remove(10000)
print("---")
print("usuniecie",liczby)
print(liczby[0:])
print(liczby[-1:0])
print("---")

print(liczby + lista)
liczby6 = liczby + lista
print(liczby6)
liczby = [1,2,3,4]
liczby2 = [5,6,7]
liczby2.extend(liczby)
print(liczby2)

tekst = 'Python'
lista_str = list(tekst)
print(lista_str)

krotka = tuple(liczby)
print(krotka)














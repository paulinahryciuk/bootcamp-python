lista = [44, 55, 66, 777, 33, 11, 33, 11]
zbior = set(lista)
print(set)
lista2 = list(zbior)
print(lista2)
lista2.remove((11))
print((lista2))

zb2 = set()
print(zb2)
print(type(zb2))
zb2.add(2)
zb2.add(3)
zb2.add(5)
zb2.add(5)
zb2.add(3)
print((zb2))
print(zb2.pop())
print(zb2)

zb2.remove(5)
print(zb2)

zbior2 = {667, 11, 44, 18, 52, 22, 667, 62, 999}
print(zbior2)

print(zbior | zbior2)
print(zbior.union(zbior2))
zbior3 = {8, 9, 10}
print(zbior.union(zbior2,zbior3))
print((zbior & zbior2))
print(zbior-zbior2)
print(zbior.difference(zbior2))

zbior4 = zbior2.copy()
print((zbior4))
zbior2.clear()
print((zbior4))
print((zbior2))
zbior2.update(zbior4)

zb3 ={1,2,3,4,5,6,8,9}
print(sum(zb3))
print((max(zb3)))
print(min(zb3))
print(len(zb3))
print((sorted((zb3))))

tupla1 = 'radek'
tupla2 = ("radek")
tupla3 = "radek",
tupla4 = ("radek",)
print(type(tupla4))

tupla5 = "Radek", "Tomek", "zenek"
print(type(tupla5))
print(tupla5)

temp = 36,6
print(type(temp))

tupla_liczby = 45,55,22.34,11,200
print(tupla_liczby)
print(type(tupla_liczby))

# del temp[0]
del temp
# print(temp)

print(tupla_liczby[:2])
print(tupla_liczby[-1])
print(tupla_liczby[0:1])
print(tupla_liczby[:])
print(tupla_liczby[0:3:2])

print(55 in tupla_liczby)
print(tupla_liczby.count(55))
print(tupla_liczby.index(11))
print((sorted(tupla_liczby)))
print((sorted(tupla_liczby, reverse= True)))

a,b = 1,2
print(type((1,2)))
#
# tupla5("BArtek","radek","tomek","zenek")
# imie1, *imie2, imie3 = tupla5


print("rad", end = '')
print("rad", "kot", sep = "-")

lista = list(tupla_liczby)
print(lista)
print(type(lista))

print(len(tupla_liczby))
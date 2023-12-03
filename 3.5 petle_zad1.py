# for i in range (10):
#     print(i,i, sep =":", end = '')
#
# imie = "Paulina"
# for i in imie:
#     print(i)
# import random
# lista = list(range(1,50))
# for n in range(1,6):
#     a=random.choice(lista)
#     lista.remove((a))
#     print(a)
#
# lista = [5,10,23,36,8,16]
# lista.sort(reverse=True)
# print(lista)

# lista = [n for n in range (1,10) if j%2==0]

lista = ["ada", 'ola', 'ania']
for i in range (len(lista)):
    print(i, lista[i])

ludzie = ["ada", 'ola', 'ania']
wiek = [10,20,30]
for n in range(len(ludzie)):
    print(ludzie[n],wiek[n])

for i in range(-10,0,2):
    print(i)

for i in range (10,0,-2):
    print(i)

c = {"name":"radek", "age":"5"}
print({v: k for k, v in c.items() })
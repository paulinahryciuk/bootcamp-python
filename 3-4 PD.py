# Zad 2

def obl_srednia (lista):
    liczba_ocen = len(lista)
    suma = 0
    try:
        for i in lista:
            suma += i
        srednia = suma/liczba_ocen
    except TypeError:
        print("Nieprawidlowe dane")
    except ValueError:
        print("Nieprawidlowe dane")
    except ZeroDivisionError:
        print("Lista z ocenami jest pusta")
    except Exception as e:
        print(f"Blad: {e}")
    else:
        print(f"Srednia ocen wynosi: {srednia}")
    finally:
        print("koniec obliczen")

lista = [3,4,5]
obl_srednia(lista)

# Nie wiem czy tutaj lista to ma byc input od uzytkownika ? Jesli tak, to nie jestem pewna czy potrafie to zrobic.

#zad 3 generator hasel
# print("Witaj w generatorze hasel")
# while True:
#     liczba_znakow = int(input("Z ilu znakow ma skaldac sie haslo ? "))
#     if liczba_znakow<5:
#         print("Haslo za krotkie! Powinno zawierac co najmniej 6 znakow")
#     else:
#         break
# while True:
#     znaki_spec = int(input("Ile znakow specjalnych ma zawierac? "))
#     if znaki_spec>liczba_znakow:
#         print("Podales wieksza liczbe znakow specjalnych niz Twoja dlugosc hasla")
#     else:
#         break
# print(f"Pozosatalo {liczba_znakow-znaki_spec} znakow do wykorzystania")
# while True:
#     cyfry = int(input("ile cyfr ma miec haslo? "))
#     if cyfry> liczba_znakow - znaki_spec:
#         print("nie masz tylu znakow do dyspozycji")
#         print(f"Pozosatalo {liczba_znakow - znaki_spec} znakow do wykorzystania")
#     else:
#         break
# print(f"Pozosatalo {liczba_znakow-znaki_spec-cyfry} znakow do wykorzystania")
# while True:
#     duze_litery = int(input("Ile z nich ma byc duza literą? "))
#     if duze_litery> liczba_znakow - znaki_spec - cyfry:
#         print(f"Masz {liczba_znakow-znaki_spec-cyfry} znakow do wykozrystania")
#     else:
#         break
# male_litery = liczba_znakow-znaki_spec-cyfry - duze_litery
# print(f"Malych liter w hasle bedzie: {male_litery}")
#
# import random
# import string
# haslo = []
# lista1 = random.choices(string.punctuation, k = znaki_spec)
# haslo.extend(lista1)
# lista2 = random.choices(string.digits, k = cyfry)
# haslo.extend(lista2)
# lista3 = random.choices(string.ascii_lowercase, k = male_litery)
# haslo.extend(lista3)
# lista4 = random.choices(string.ascii_uppercase, k = duze_litery)
# haslo.extend(lista4)
# random.shuffle(haslo)
# print(f" Twoje haslo: {''.join(haslo)}")

#Zad 5 liczba pierwsza


# def jest_pierwsza (liczba):
#     lista_dzielnikow = []
#     for i in range(1,liczba):
#         if liczba % i !=0:
#             lista_dzielnikow.append(i)
#             if len(lista_dzielnikow)>2:
#                 print ("false")
#
# liczba = int(input("Podaj liczbe: "))
# jest_pierwsza (liczba)

# def funkcja (liczba):
#     print("Podaj liczbe")
#     def jest_pierwsza(liczba):
#         print("liczba pierwsza")
#     def nie_jest_pierwsza(liczba):
#         print("liczba nie jest pierwsza")
#
#     lista_dzielnikow = []
#     for i in range(1,liczba):
#         if liczba % i !=0:
#             lista_dzielnikow.append(i)
#         if len(lista_dzielnikow)>2:
#             return nie_jest_pierwsza()
#         else:
#             return jest_pierwsza()
#
# pierwsza = funkcja()

#rozwiazanie
# def czy_pierwsza (liczba):
#     lista_dzielnikow = []
#     for i in range(1,liczba):
#         if liczba % i !=0:
#             lista_dzielnikow.append(i)
#         if len(lista_dzielnikow)>2:
#             return False
#         else:
#             return True
#
# czy_pierwsza (3)
# #niestety nie dziala:(

#zadanie 1

tekst = input("Podaj swoj teskt: ")

def podziel(tekst):
    global podzielony
    podzielony = tekst.split(" ")
    print(f"Twoj tekst sklada sie ze slow: {podzielony} ")

try:
    podziel(tekst)
    2/len(tekst)

    slownik = {}  # mialo byc przez def
    for i in podzielony:
        a = podzielony.count(i)
        print(f"slowo {i} wystepuje {a} razy")
        slownik[i] =a
    print("slownik z liczba wsytapien: " , slownik)

#filtracja
except ValueError:
    print("Blad wartosci")
except ZeroDivisionError:
    print("Twoj tekst jest pusty")
else:
    print("Twoj tekst jest prawidlowy")
finally:
    print("koiec pracy")




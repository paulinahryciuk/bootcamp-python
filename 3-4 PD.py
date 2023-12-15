# Zadanie 2

def obl_srednia(lista):
    liczba_ocen = len(lista)
    suma = 0
    try:
        for i in lista:
            suma += i
        srednia = suma / liczba_ocen
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


lista = [3, 4, 5]
obl_srednia(lista)

# Nie wiem czy tutaj lista to ma byc input od uzytkownika ?

#zadanie 3

print("Witaj w generatorze hasel")
while True:
    liczba_znakow = int(input("Z ilu znakow ma skaldac sie haslo ? "))
    if liczba_znakow < 5:
        print("Haslo za krotkie! Powinno zawierac co najmniej 6 znakow")
    else:
        break
while True:
    znaki_spec = int(input("Ile znakow specjalnych ma zawierac? "))
    if znaki_spec > liczba_znakow:
        print("Podales wieksza liczbe znakow specjalnych niz Twoja dlugosc hasla")
    else:
        break
print(f"Pozosatalo {liczba_znakow - znaki_spec} znakow do wykorzystania")
while True:
    cyfry = int(input("ile cyfr ma miec haslo? "))
    if cyfry > liczba_znakow - znaki_spec:
        print("nie masz tylu znakow do dyspozycji")
        print(f"Pozosatalo {liczba_znakow - znaki_spec} znakow do wykorzystania")
    else:
        break
print(f"Pozosatalo {liczba_znakow - znaki_spec - cyfry} znakow do wykorzystania")
while True:
    duze_litery = int(input("Ile z nich ma byc duza literą? "))
    if duze_litery > liczba_znakow - znaki_spec - cyfry:
        print(f"Masz {liczba_znakow - znaki_spec - cyfry} znakow do wykozrystania")
    else:
        break
male_litery = liczba_znakow - znaki_spec - cyfry - duze_litery
print(f"Malych liter w hasle bedzie: {male_litery}")

import random
import string

haslo = []
lista1 = random.choices(string.punctuation, k=znaki_spec)
haslo.extend(lista1)
lista2 = random.choices(string.digits, k=cyfry)
haslo.extend(lista2)
lista3 = random.choices(string.ascii_lowercase, k=male_litery)
haslo.extend(lista3)
lista4 = random.choices(string.ascii_uppercase, k=duze_litery)
haslo.extend(lista4)
random.shuffle(haslo)
print(f" Twoje haslo: {''.join(haslo)}")


# Zad 5 liczba pierwsza


def jest_pierwsza(liczba):
    lista_dzielnikow = []
    for i in range(1, liczba):
        if liczba % i == 0:
            lista_dzielnikow.append(i)
    if liczba == 1:
        print("Liczba musi byc wieksza od 1")
    elif len(lista_dzielnikow) >= 2:
        print("Czy jest liczba pierwsza?")
        print(bool(0))
    else:
        print("Czy jest liczba pierwsza?")
        print(bool(1))


liczba = int(input("Podaj liczbe: "))
jest_pierwsza(liczba)

# zadanie 1

tekst = input("Podaj swoj teskt: ")
filtr = input("Czy ktres slowo ktore chcesz pominac w analizie: ")
tekst_temp = tekst.replace(filtr, "")
print(f"Twoj nowy tekst to: {tekst_temp}")
slownik = {}


def podziel(tekst_temp):
    global podzielony
    podzielony = tekst_temp.strip().replace("  ", " ").split(" ")
    print(f"Twoj tekst sklada sie ze slow: {podzielony} ")


def zlicz(podzielony):
    for i in podzielony:
        a = podzielony.count(i)
        slownik[i] = a
    print("slownik z liczba wsytapien: ", slownik)


try:
    podziel(tekst_temp)
    2 / len(tekst_temp)
    zlicz(podzielony)



except ValueError:
    print("Blad wartosci")
except ZeroDivisionError:
    print("Twoj tekst jest pusty")
else:
    print("Analiza przebiegla pomyslnie")
finally:
    print("Koniec pracy")



# Zad 4
lista1 = [1, 2, "A"]
lista2 = [3, 2, "A"]


def unikalne(lista1, lista2):
    print(list(set(lista1) & set(lista2)))


unikalne(lista1, lista2)
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
print("Witaj w generatorze hasel")
while True:
    liczba_znakow = int(input("Z ilu znakow ma skaldac sie haslo ? "))
    if liczba_znakow<5:
        print("Haslo za krotkie! Powinno zawierac co najmniej 6 znakow")
    else:
        break
while True:
    znaki_spec = int(input("Ile znakow specjalnych ma zawierac? "))
    if znaki_spec>liczba_znakow:
        print("Podales wieksza liczbe znakow specjalnych niz Twoja dlugosc hasla")
    else:
        break
print(f"Pozosatalo {liczba_znakow-znaki_spec} znakow do wykorzystania")
while True:
    cyfry = int(input("ile cyfr ma miec haslo? "))
    if cyfry> liczba_znakow - znaki_spec:
        print("nie masz tylu znakow do dyspozycji")
        print(f"Pozosatalo {liczba_znakow - znaki_spec} znakow do wykorzystania")
    else:
        break
print(f"Pozosatalo {liczba_znakow-znaki_spec-cyfry} znakow do wykorzystania")
while True:
    duze_litery = int(input("Ile z nich ma byc duza literą? "))
    if duze_litery> liczba_znakow - znaki_spec - cyfry:
        print(f"Masz {liczba_znakow-znaki_spec-cyfry} znakow do wykozrystania")
    else:
        break
male_litery = liczba_znakow-znaki_spec-cyfry - duze_litery
print(f"Malych liter w hasle bedzie: {male_litery}")

import random
import string
haslo = []
lista1 = random.choices(string.punctuation, k = znaki_spec)
haslo.extend(lista1)
lista2 = random.choices(string.digits, k = cyfry)
haslo.extend(lista2)
lista3 = random.choices(string.ascii_lowercase, k = male_litery)
haslo.extend(lista3)
lista4 = random.choices(string.ascii_uppercase, k = duze_litery)
haslo.extend(lista4)
random.shuffle(haslo)
print(f" Twoje haslo: {''.join(haslo)}")


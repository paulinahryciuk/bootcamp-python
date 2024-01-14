class MyClass:
    counter = 0

    @classmethod
    def increment_counter(cls):
        cls.counter += 1
        return cls.counter

print(MyClass.increment_counter())
print(MyClass.increment_counter())
print(MyClass.increment_counter())
c = MyClass()
print((c.increment_counter()))

class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    @classmethod
    def z_nazw_peln(cls,nazwa_pelna):
        imie, nazwisko = nazwa_pelna.split()
        return cls(imie, nazwisko)

o1 = Osoba("jan", "kowalski")
o2 = Osoba.z_nazw_peln("ann now")
print(o1.nazwisko)
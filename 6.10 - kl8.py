class Ptak:
    """
    kl opis ptaka
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.sszybkosc = szybkosc

    def latam(self):
        print(f"tu {self.gatunek} latam z szybkosci {self.sszybkosc}")

    def wydaj_odglos(self):
        pass
class Kura (Ptak):
    def __init__(self,gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print(f"tu {self.gatunek} ja nei latam")

    def wydaj_odglos(self):
        print("koko")

                         )
or1 = Ptak("orzel", 40)
or1.latam()

kur1 = Ptak("kura", 0)
kur1.latam()


class Matematyka:

    @staticmethod
    def dodaj(a,b):
        return a+b

    @staticmethod
    def odejmij(a,b):
        return a- b

wynik = Matematyka.dodaj(5,6)
print(wynik)
print(Matematyka.odejmij(9,7))


class KalkulatorTemp:

    @staticmethod
    def celc_na_fere(celc):
        pass

    @staticmethod
    def fer_na_cel(fere):
        return (fere- 32)*5/9

print(KalkulatorTemp.fer_na_cel(100))


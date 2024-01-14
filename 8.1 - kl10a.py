class Pojazd:
    def serwis(self):
        print("serwisow pojazdu")

class SamochodOsobowy(Pojazd):
    def serwis(self):
        print("serw pojaz osob")

class SamochodDostawczy(Pojazd):
    def serwis(self):
        print("Ser sam dost")

class PojazdSluzbowy(Pojazd):
    def rejestracja_sluzbowa(self):
        print("rejst poj sluz")
class SamochSluzbOsob(SamochodOsobowy,PojazdSluzbowy):
    pass

if __name__ == '__main__':
 car1 = SamochSluzbOsob()
 car1.serwis()
 car1.rejestracja_sluzbowa()
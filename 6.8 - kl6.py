class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedsatw_sie(self):
         print(f"czesc , jestem {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja

pracownik = Pracownik("Jan", "Kowalski", 5000)
pracownik.przedsatw_sie()
wyn_prac = pracownik.oblicz_pensje()
print ( f"wynagrodzeni dla pracownika { pracownik.imie} {pracownik.nazwisko}: {wyn_prac}")

class Manager(Pracownik):
    def __init__(self,imie, nazwisko, pensja,premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.premia + self.pensja

manager = Manager("anna", "kowalska",100000,20)

manager.przedsatw_sie()
print(manager.oblicz_pensje())


class Human:
    """
    Klasa Humna ops czlow
    """
    imie = ''
    wiek = "None"
    plec  = "k"

    def powitanie(self):
        print(f"nazywam sie {self.imie}")

    def wiekow(self):
        print(f"mam {self.wiek} lat")

cz1 = Human()
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)

cz2 = Human()
cz2.imie = "Adam"
cz2.wiek = 30
cz2.plec = "m"

print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
cz2.powitanie()
cz2.wiekow()
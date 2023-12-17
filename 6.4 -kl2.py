class Human:
    '''
    Kasa Human opisujaca czlowieka w pythonie
    '''

    def __init__(self, imie, wiek, wzrost, plec = "k"):
        '''

        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        '''
        self.imie = imie
        self.wiek = wiek
        self.plec = plec
        self.wzrost = wzrost
    def powitanie(self):
        print(f"nazywam sie {self.imie}")

    def wiekow(self):
        print(f"mam {self.wiek} lat")

    def podaj_wzrost(self):
        print(f"mam {self.wzrost}")

    def ruszaj(self):
        if self.plec =="m":
            print("rusz-em")
        else:
            print("rusz-am")


cz1 = Human("anna",27,170)
print(cz1)
print(cz1.imie)
print(cz1.__doc__)
print(cz1.__init__.__doc__)
cz1.powitanie()
cz1.podaj_wzrost()

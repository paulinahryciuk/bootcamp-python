class Dom:
    """
    kl opis dom
    """

    def __init__(self,metraz,kolor,l_okien):
        self.__metraz = metraz
        self.kolor = kolor
        self.l_okien = l_okien

    def wyswietl_okna(self):
        print(f"mam{self.l_okien}")

    def zwroc_metraz(self):
        print(f"metrarz {self.__metraz}")

    def zmien_metraz(self):
        self.__metraz = 80



d1 = Dom(60,"bialy",10)
# print(d1.__metraz)
# print(d1.kolor)
# print(d1.l_okien)
d1.wyswietl_okna()
d1.__metraz = 50
# print(d1.__metraz) tak nei mozna
d1.zmien_metraz()
d1.zwroc_metraz()

class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor


    def info(self):
        print(f"kolor {self.kolor}")

class Samochod(Pojazd):
    """
    samochod
    """

poj = Pojazd("Czerwony")
poj.info()
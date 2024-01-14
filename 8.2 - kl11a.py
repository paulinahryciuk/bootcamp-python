from abc import ABC, abstractmethod

class Counter(ABC):
    def __init__(self, values = 0):
        self.values = values

    def increment(self, by=1):
        self.values += by

    @abstractmethod
    def drukuj(self):
        pass

class NewCounter(Counter):
    """
    licznik bez metody drukuj
    """

class BounderCounter(Counter):
    MAX = 100
    def __init__(self, values):
        if values> self.MAX:
            raise ValueError(f"wart nei moze byc wieksz od {self.MAX}")
        super().__init__(values)




    def drukuj(self):
        print("drukuje".self.values)

c1 = BounderCounter()
c1.drukuj()
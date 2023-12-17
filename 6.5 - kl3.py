class Car:
    """
    kl op auto w pyth
    """

    def __init__(self,model,year):
        self.model = model
        self.year = year
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

car1 = Car("bmw", 2023)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
print(car1.__predkosc)


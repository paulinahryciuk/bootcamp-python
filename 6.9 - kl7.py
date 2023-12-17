class Animal:
    def __init__(self, name):
        self.name = name
    def wydaj_odglos(self):
        pass

    def info(self):
        print(f"imie {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def wydaj_odglos(self):
        print("hau")

    def info(self):
        super().info()
        print(f"rasa : {self.breed}")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def info(self):
        super().info()
        print(f"kolor { self.color}")

    def wydaj_odglos(self):
        print("miau")

class Tiger(Cat):

    def __init__(self, name, color,liczba_paskow):
        super().__init__(name, color)
        self.liczba_paskow = liczba_paskow

    def wydaj_odglos(self):
        print("aarr")

    def info(self):
        super().info()
        print(f"liczba pskow {self.liczba_paskow}")

animal1 = Animal("Bezimienny")
animal1.info()
animal1.wydaj_odglos()

dog1 = Dog("Burek", "kundel")
dog1.info()
dog1.wydaj_odglos()

cat1 = Cat("filemon","Bialy w ciapy")
cat1.info()
cat1.wydaj_odglos()

tyg1 = Tiger("tygrysek", "pomaranczowy",15)
tyg1.info()
tyg1.wydaj_odglos()


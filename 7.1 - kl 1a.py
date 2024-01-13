import math

class MyFirstClass:
    """
    kl w pythonie op punkty w przestrzeni
    """

    def __init__(self, x= 0, y=0):
        """
        fun inicjalozujaca
        :param x:
        :param y:
        """
        self.x = x
        self.y = y

    def move(self, x:float, y:float):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0,0)

    def calculate(self,other: "MyFirstClass") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


    def __str__(self):
        return f"({self.x,self.y})"

ob = MyFirstClass()
print((ob))
print((ob.x))
print((ob.y))
print(ob)

ob2 = MyFirstClass(5,7)
print(ob2)

lista_punkty = [ob,ob2]
print(lista_punkty)
print("____________")

ob3 = MyFirstClass(10,20)
ob4 = MyFirstClass(15,30)
print(ob3)
print(ob4)
print(ob3.calculate(ob4))
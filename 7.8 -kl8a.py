class A:
    def method(self):
        print("Metoda z klasy A")

class B(A):
    def method(self):
        print("Metoda z klasy B")

class C(A):
    def method(self):
        print("Metoda z klasy C")

class D(B,C):
    pass

d = D()
d.method()
print(D.__mro__)
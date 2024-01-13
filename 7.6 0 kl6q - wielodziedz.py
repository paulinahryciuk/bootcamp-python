class A:
    def method(self):
        print("medoda kl a")


class B:
    def method(self):
        print("medoda kl b")

class C(B,A):
    """
    dzidzicz A i B
    """
class E (A,B):
    def method(self):
        print("metoda E")


class F(B,A):

    def method(self):
        A.method(self)


class G(A,B):

    def super().classmethod
    pr
a = A()
a.method()

b = B()
b.method()

c= C()
c.method()
e = E()
e.method()
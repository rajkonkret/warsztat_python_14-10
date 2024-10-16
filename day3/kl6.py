class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasy B")


class C(B, A):
    """
    Klasa dziedziczy po klasie A i B
    """


a = A()
a.method()
b = B()
b.method()
# Metoda z klasy A
# Metoda z klasy B

c = C()
c.method()  # Metoda z klasy B
print(C.__mro__)


# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

class D(A, B):
    """
    Kalsa dziedziczy po B i A"""


d = D()
d.method()  # Metoda z klasy A


class E(A, B):
    def method(self):
        print("Metoda z klasy E")


e = E()
e.method()  # Metoda z klasy E


class F(A, B):
    def method(self):
        B.method(self)  # jawne wywołanie metody z klasy B


f = F()
f.method()  # Metoda z klasy B


class G(A, B):
    def method(self):
        super().method()  # super() - klasa nadrzędna tutaj A
        print("Dopisane")


g = G()
g.method()
# Metoda z klasy A
# Dopisane

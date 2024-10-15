# klasy - element programowania obiektowego
# szablon, przepis, stempel, matryca
# obiekt (instancja) - zbudowany wg przepisu, ciasto, odcisk stempla
# hermetyzacja, polimorfizm, dziedziczenie, abstrakcja
# Klasa nakreśła cechy i funkcje jakie będzie posiadałą obiekt

import math


class MyFirstClass:
    """
    Klasa w Pythonie, opisujaca punkty w przestrzeni x, y
    """

    def __init__(self, x=0, y=0):
        """
        Funkcja incjalizująca (konstruktor)
        :param x:
        :param y:
        """
        # self - obiekt, który wywołuje metode
        # self.x = x
        # self.y = y
        self.move(x, y)

    def move(self, x: int, y: int) -> None:
        """
        Funkcja przemieszcza obiekt we wskazane miejsce
        :param x:
        :param y:
        :return:  None
        """
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:
        """
        Obliczenie odległości między dwoma punktami w przestrzeni Euklidesowej
        :param other:
        :return:  float
        """
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):  # opis obiektu
        return f"{self.x, self.y}"

    def __repr__(self):  # reprezentacja obiektu
        return f"Point({self.x, self.y})"


print(MyFirstClass.__doc__)  # Klasa w Pythonie, opisujaca punkty w przestrzeni x, y
ob = MyFirstClass()
print(ob)  # <__main__.MyFirstClass object at 0x0000015C34F6C050>
# Po nadpisaniu metody __str__ print wypisze obiekt tak: (0, 0)
print(ob.x)
print(ob.y)
ob.move(45, 78)
print(ob)  # (45, 78)
ob.reset()
print(ob)  # (0, 0)

ob2 = MyFirstClass(78, 94)
print(ob2)  # (78, 94)
print(ob.calculate(ob2))  # 122.14745187681976
# print(ob.calculate(200))  # Pycharm sugeruje, ze pomyliłeś typ
print(ob2.calculate(ob))  # 122.14745187681976

lista = [ob, ob2]
print(lista)
# [<__main__.MyFirstClass object at 0x0000019BC226E450>, <__main__.MyFirstClass object at 0x0000019BC226EF30>]
# Po nadpisaniu metody __repr__
# [Point((0, 0)), Point((78, 94))] -> __repr__
for p in lista:
    print(p)  # __str__
# (0, 0)
# (78, 94)

from abc import ABC, abstractmethod


class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by

    @abstractmethod  # metoda abstrakcyjna
    def drukuj(self):
        pass

    @staticmethod
    def from_string():
        print("Metoda statyczna")

    @classmethod  # zamiennik konstruktorów, przeciązanie
    def from_counter(cls, counter):
        return cls(counter.values)


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values):
        if values > self.MAX:
            raise ValueError(f"Wartość nie może być większa niż {self.MAX}")
        super().__init__(values)

    def drukuj(self):
        print("Drukuje", self.values)


# TypeError: Can't instantiate abstract class NewCounter without an implementation for abstract method 'drukuj'
class NewCounter(Counter):
    """
    Klasa NewCounter
    """


class SecondCounter(Counter):
    """
    Klasa dziedziczy po counter
    """

    def drukuj(self):
        print("Drukuj", self.values)


# klasa oznaczona jako abstrakcyjna, nie mozna tworzyc obiektu tej klasy
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\warsztat_python_14-10\day3\kl10.py", line 28, in <module>
#     c1 = Counter()
#          ^^^^^^^^^
# TypeError: Can't instantiate abstract class Counter without an implementation for abstract method 'drukuj'
# c1 = Counter()
# c1.increment()
# c1.drukuj()

bd = BoundedCounter(10)
bd.increment()
bd.drukuj()  # Drukuje 11

# nc = NewCounter() # TypeError: Can't instantiate abstract class NewCounter without an implementation for abstract method 'drukuj'

# metoda statyczna
Counter.from_string()  # Metoda statyczna

# metoda classmethod
bd2 = BoundedCounter.from_counter(bd)
bd2.drukuj()  # Drukuje 11

bd3 = BoundedCounter(bd2.values)
bd3.drukuj()

sc = SecondCounter()
sc.drukuj()

# polimorfizm  -obiekty różnych klas dzieki dziedziczeniu i abstrakcji mają wspołne cechy i metody
lista = [bd, bd2, bd3, sc]
for i in lista:
    i.drukuj()
# Drukuje 11
# Drukuje 11
# Drukuje 11
# Drukuj 0

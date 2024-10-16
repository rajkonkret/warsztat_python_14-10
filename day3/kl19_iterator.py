# lazy - leniwy

lista = [1, 2, 3, 4, 5]
iterator = iter(lista)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# 1
# 2
# 3
print("Coś innego")
print(next(iterator))
# Coś innego
# 4
print(next(iterator))


# print(next(iterator))
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\warsztat_python_14-10\day3\kl19_iterator.py", line 15, in <module>
#     print(next(iterator))
#           ^^^^^^^^^^^^^^
# StopIteration
class Count:
    def __init__(self, lows, high):
        """
        metoda inicjalizująca
        :param lows:  start
        :param high:  stop
        """
        self.current = lows
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1  # zmieniam stan pola current o 1
            return self.current - 1  # zwracam napis o jeden mniejszy


print("----------")
counter = Count(1, 5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
# ----------
# 1
# 2
# 3
# 4
# 5
print(next(counter))
# Process finished with exit code 1
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\warsztat_python_14-10\day3\kl19_iterator.py", line 57, in <module>
#     print(next(counter))
#           ^^^^^^^^^^^^^
#   File "C:\Users\CSComarch\PycharmProjects\warsztat_python_14-10\day3\kl19_iterator.py", line 39, in __next__
#     raise StopIteration
# StopIteration

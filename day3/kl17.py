# print(2 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\warsztat_python_14-10\day3\kl17.py", line 1, in <module>
#     print(2 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
# raise ZeroDivisionError
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\warsztat_python_14-10\day3\kl17.py", line 7, in <module>
#     raise ZeroDivisionError
# ZeroDivisionError
# raise ZeroDivisionError("Nie dziel przez zero")
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\warsztat_python_14-10\day3\kl17.py", line 12, in <module>
#     raise ZeroDivisionError("Nie dziel przez zero")
# ZeroDivisionError: Nie dziel przez zero
class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


# pobierzemy liczby cąlkowite od użytkownika
# gdy poda mniejszą od zera, rzucimy wyjątek MyException
# obsłużymy ten wyjątek
# raise MyException("Liczba musi być większa od zera") # MyException: Liczba musi być większa od zera
try:
    x = int(input("Podaj liczbę całkowitą większą od zera"))
    if x <= 0:
        raise MyException("Liczba musi być większa od zera")
except MyException:
    print("Wartość musi być większa od zera")
except Exception as e:
    print("Bład", e)
else:
    print("Podana wartość", x)
finally:
    print("Koniec")
# Podaj liczbę całkowitą większą od zera12
# Podana wartość 12
# Koniec
# Podaj liczbę całkowitą większą od zera-9
# Wartość musi być większa od zera
# Koniec

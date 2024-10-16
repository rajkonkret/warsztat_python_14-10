class MyError(Exception):
    def __init__(self, message, err_code):
        super().__init__(message)
        self.err_code = err_code


class MyValueError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=100)


class MyTypeError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=200)


def my_function(x: int, y: int) -> float:
    if not isinstance(x, int):
        raise MyTypeError("x must be integer")
    if not isinstance(y, int):
        raise MyTypeError("y must be integer")
    if y == 0:
        raise MyValueError("y cannot be zero")

    return x / y


while True:
    try:
        a = input("Podaj pierwszą liczbę")
        b = input("Podaj drugą liczbę")
        if a == "q" or b == "q":
            break
        result = my_function(int(a), int(b))
    except MyTypeError:
        print("MyTypError")
    except MyValueError:
        print("Dzielenie przez zero")
    except ValueError:
        print("Bład wartości")
    except TypeError:
        print("Bład typu")
    except Exception as e:
        print("Błąd", e)
    else:
        print(f"Wynik wynosi {result}")
    finally:
        print("Koniec")
# Podaj pierwszą liczbę1
# Podaj drugą liczbę2
# Wynik wynosi 0.5
# Koniec
# Podaj pierwszą liczbę2
# Podaj drugą liczbę0
# Dzielenie przez zero
# Koniec
# Podaj pierwszą liczbęa
# Podaj drugą liczbęb
# Bład wartości
# Koniec
# Podaj pierwszą liczbę
# Podaj pierwszą liczbęq
# Podaj drugą liczbęq
# Koniec
# my_function("A", 12)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\warsztat_python_14-10\day3\kl18.py", line 65, in <module>
#     my_function("A", 12)
#   File "C:\Users\CSComarch\PycharmProjects\warsztat_python_14-10\day3\kl18.py", line 19, in my_function
#     raise MyTypeError("x must be integer")
# MyTypeError: x must be integer
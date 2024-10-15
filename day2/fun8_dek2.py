# zrobić dekorator, który zamienia wynik działania funkcji na duże litery
# funkcje która zwraca tekst
# dekorator, który wypisze pogrubionymi lliterkami bold_decorator)
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        # *args - dowolna ilość argumentów pozycyjnych
        # **kwargs - dowolna ilość argumentów nazwanych (a=0)
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


def bold_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"\033[1m" + result + "\033[0m"

    return wrapper


@bold_decorator
@uppercase_decorator
def greeting():
    return "Hello World!!!"


@uppercase_decorator
def greeting2(string):
    return f"Podałeś {string}"


print(greeting())  # HELLO WORLD!!!
print(greeting2("Radek"))
# HELLO WORLD!!!
# PODAŁEŚ RADEK

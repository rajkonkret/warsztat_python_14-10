# stworzenie raportu
# generator to wygenerowania danych
# przetworzone dane
# stworzony raport
# pomiar czasu (dekorator)
import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")

        return result

    return wrapper


def generataor_danych(dane):
    for element in dane:
        yield element


def przetworz_dane(dane):
    return [element for element in dane if element % 2 == 0]


@measure_time
def stworz_raport(dane):
    for element in generataor_danych(dane):
        print(f"Raport dla systemu {element}")


dane = range(100_000)
pr_dane = przetworz_dane(dane)
stworz_raport(pr_dane)
# Raport dla systemu 99992
# Raport dla systemu 99994
# Raport dla systemu 99996
# Raport dla systemu 99998
# Czas wykonania funkcji stworz_raport: 0.8755383491516113

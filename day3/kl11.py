class Matematyka:
    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b


print(Matematyka.dodaj(56, 78))


class KalkulatorTemperatur:

    @staticmethod
    def celcius_fahrenheit(celcius):
        return celcius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_celcius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9


print(KalkulatorTemperatur.fahrenheit_celcius(100))
print(KalkulatorTemperatur.celcius_fahrenheit(36.6))
# 37.77777777777778
# 97.88000000000001

# funkcja - wydzielony fragment kodu, który można wykonywac wielokrotnie


a = 10
b = 15


# deklaracji funkcji
def dodaj():
    print(a + b)


def dodaj2(a, b):  # dwa obowiązkowe do przekazania argumenty
    print(a + b)


# podpowiedzi typó
def odejmij(a: int, b: int, c=0):  # c=0 ma wartośc domyslną
    print(a - b - c)


def mnozenie(a: int, b: int) -> int:
    return a * b  # zwraca wynik


def mnozenie2(a, b):
    return a, b, a * b


# uruchomienie funkcji
dodaj()  # 25
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'

# argumenty pozycyjne
dodaj2(56, 89)
odejmij(1, 45)
odejmij(1, 4, 765)

# argumenty nazwane
odejmij(b=9, c=90, a=34)

# mieszane
odejmij(1, c=90, b=87)
print(dodaj())
# 25
# None
print(mnozenie(6, 23))  # 138
a = mnozenie(6, 9)
print("Wynik", a)  # Wynik 54

print(mnozenie(6, 4) + mnozenie(5, 9))  # 69
# print(dodaj() + dodaj2(6, 8))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

b = mnozenie2(56, 90)
print(b)  # (56, 90, 5040) a,b  =wynik ->
# wynik działania 56 * 90 = 5040
x, y, z = mnozenie2(56, 90)
print(f"Wynik działania: {x} * {y} = {z}")  # Wynik działania: 56, 90, 504
# (56, 90, 5040)
# Wynik działania: 56 * 90 = 5040

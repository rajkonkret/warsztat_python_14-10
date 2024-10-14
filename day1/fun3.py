# lambda - skrocony zapis funkcji
# lambda ma return
# funkcja anonimowa - mozliwosc użycia w miejscu deklaracji
from functools import reduce, lru_cache


def liczymy(x, y):
    return x * y


print(liczymy(6, 9))  # 54

liczymy2 = lambda x, y: x * y
print(liczymy2(4, 7))  # 28

# mapowanie
lista = [1, 2, 5, 10, 100, 200, 500]

# nowa lista z wartosciami x ** 2
lista2 = []
for i in lista:
    lista2.append(i ** 2)
print(lista2)  # [1, 4, 25, 100, 10000, 40000, 250000]

print([i ** 2 for i in lista])  # [1, 4, 25, 100, 10000, 40000, 250000]


def zmien(x):
    return x ** 2


lista3 = []
for i in lista:
    lista3.append(zmien(i))

print(lista3)  # [1, 4, 25, 100, 10000, 40000, 250000]

# funkcje wyższego rzędu
# map(), filter(), reduce(), lru_cache()

print(f"Zastosowanie map() {list(map(zmien, lista))}")
# Zastosowanie map() [1, 4, 25, 100, 10000, 40000, 250000]

# zastosowanie lambdy jako funkcji anonimowej
print(f"Zastosowanie map() {list(map(lambda x: x ** 2, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x / 2, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x ** 3, lista))}")
# Zastosowanie map() [1, 4, 25, 100, 10000, 40000, 250000]
# Zastosowanie map() [1, 4, 25, 100, 10000, 40000, 250000]
# Zastosowanie map() [2, 4, 10, 20, 200, 400, 1000]
# Zastosowanie map() [0.5, 1.0, 2.5, 5.0, 50.0, 100.0, 250.0]
# Zastosowanie map() [1, 8, 125, 1000, 1000000, 8000000, 125000000]

# filter()

for i in lista:
    if i < 10:
        print(i)

print(f"Uzycie filter() {list(filter(lambda x: x < 5, lista))}")
print(f"Uzycie filter() {list(filter(lambda x: x > 25, lista))}")
print(f"Uzycie filter() {list(filter(lambda x: x > 5 and x < 300, lista))}")
print(f"Uzycie filter() {list(filter(lambda x: 5 < x < 300, lista))}")
# Uzycie filter() [1, 2]
# Uzycie filter() [100, 200, 500]
# Uzycie filter() [10, 100, 200]
# Uzycie filter() [10, 100, 200]

r0 = {'miasto': 'Kielce'}
r1 = {'miasto': "Kielce", "ZIP": "25-900"}
print(r0['miasto'])
print(r1['miasto'])
# Kielce
# Kielce
print(r1['ZIP'])
# print(r0['ZIP'])  # KeyError: 'ZIP'

print(r0.get('ZIP', "00-000"))

d_zip = lambda row: row.setdefault("ZIP", "00-000")
print(d_zip(r0))
print(d_zip(r1))
# 25-900
# 00-000
# 00-000
# 25-900
print(r1)
print(r0)
# {'miasto': 'Kielce', 'ZIP': '25-900'}
# {'miasto': 'Kielce', 'ZIP': '00-000'}

lata = [(2000, 29.7), (2001, 33.12), (2010, 32.92)]
print(max(lata))
print(min(lata))
# (2010, 32.92)
# (2000, 29.7)

print(max(lata, key=lambda c: c[1]))  # (2001, 33.12)
print(max(map(lambda c: (c[1], c), lata)))  # (33.12, (2001, 33.12))
print(max(map(lambda c: c[1], lata)))  # 33.12
print(max(map(lambda c: (c[1], c[0]), lata)))  # (33.12, 2001)

# reduce()
liczby = [1, 2, 3, 4, 5]
wynik = reduce(lambda a, b: a + b, liczby)
"""
    reduce(function, iterable[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of a sequence
    or iterable, from left to right, so as to reduce the iterable to a single
    value.  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the iterable in the calculation, and serves as a default when the
    iterable is empty.
    """
print(wynik)  # 15
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4  = 10
# 10 + 5 = 15
wynik_mnozenie = reduce(lambda a, b: a * b, liczby)
print("Wynik mnożenia reduce()", wynik_mnozenie)  # Wynik mnożenia reduce() 120


# ((((1*2)*3)*4)*5)

@lru_cache(maxsize=1000)
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


print(fib_cached(10))
print(fib_cached.cache_info())
# CacheInfo(hits=8, misses=11, maxsize=1000, currsize=11)
print(fib_cached(5))
print(fib_cached.cache_info())
# CacheInfo(hits=9, misses=11, maxsize=1000, currsize=11)
# hits = ile razy uzyskał wynik nie musząc wykonać obliczen
# misses - ile razy wykonywał obliczenia
fib_cached.cache_clear()  # czyszczenie cache
print(fib_cached.cache_info())  # CacheInfo(hits=0, misses=0, maxsize=1000, currsize=0)

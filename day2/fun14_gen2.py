from day1.typy_danych_2_kolekcje import lista

generator_1 = [x for x in range(5)]
print(generator_1)  # [0, 1, 2, 3, 4]
print(type(generator_1))  # <class 'list'>

generator_2 = (x for x in [1, 2, 3, 4, 5])  # to jest generator
print(type(generator_2))  # <class 'generator'>
print(generator_2)  # <generator object <genexpr> at 0x0000026CD7A1CE80>

print(next(generator_2))
print(next(generator_2))
print(next(generator_2))
print(next(generator_2))
print(next(generator_2))


def generator3():
    for x in [1, 2, 3, 4, 5]:
        yield x


g3 = generator3()
print(next(g3))
print(next(g3))
print(next(g3))


# 1
# 2
# 3

def gen4():
    i = 1
    while True:
        yield i * i
        i += 1


g4 = gen4()
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))


def fibo():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


fib1 = fibo()
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))


def fibo_with_index(n):
    a, b = 0, 1
    for ind in range(n):
        yield ind, a
        a, b = b, a + b


fib2 = fibo_with_index(10)
print(next(fib2))
print(next(fib2))
print(next(fib2))
print(next(fib2))
print(next(fib2))
# (0, 0)
# (1, 1)
# (2, 1)
# (3, 2)
# (4, 3) -> i, n

for i, n in fibo_with_index(10):
    print(f"Pozycja {i}, element {n}")
# Pozycja 0, element 0
# Pozycja 1, element 1
# Pozycja 2, element 1
# Pozycja 3, element 2
# Pozycja 4, element 3
# Pozycja 5, element 5
# Pozycja 6, element 8
# Pozycja 7, element 13
# Pozycja 8, element 21
# Pozycja 9, element 34

fibo3 = fibo_with_index(10)
print(list(fibo3))
print("-------")
for i in fibo3:
    print(i)
    # list() - wyczerpało generator
    # nie ma kolejnych elemntów
# [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34)]
# -------

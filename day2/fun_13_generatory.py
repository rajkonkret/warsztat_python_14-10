# generatory - generuje wartość dla danego argumentu

def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


# 0
# 1
# 4
# 9
# 16

def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # zwraca wynik i ustawia wskaźnik na następny


kwa = kwadrat2(5)
print(kwa)  # <generator object kwadrat2 at 0x0000019F943035E0
print(next(kwa))
print(next(kwa))
print(next(kwa))  # 4
print("Zrób cokolwiek")
lista = []
lista.append("123456")
print(lista)

print(next(kwa))
print(next(kwa))
# print(next(kwa))  # StopIteration - gdy wyczerpiemy dane z generatora


kwa2 = kwadrat2(10)
kwa3 = kwadrat2(20)

print(next(kwa2))
print(next(kwa3))
print(next(kwa2))
print(next(kwa3))

print(list(kwa3))
# [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]

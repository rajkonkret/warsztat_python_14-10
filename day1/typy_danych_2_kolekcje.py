# kolekcje - moze przechowywać dowolną ilość wartośći
# lista, krotka (tupla), set(zbiór), słownik

# lista  - podstawowa kolecja, zachowuje kolejnosc przy dodawaniau elementów
lista = []
lista = list()
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Marek")
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Marek']
lista_copy = lista.copy()
lista2 = lista
print(lista2)
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Marek']
# ['Radek', 'Tomek', 'Zenek', 'Marek']
print(id(lista))  # 2399973752768
print(id(lista2))  # 2399973752768
lista.clear()
print(lista2)
print(lista)
# []
# []
print(lista_copy)  # ['Radek', 'Tomek', 'Zenek', 'Marek']

# krotka, tupla - niemutowalna kolekcja
# krotka pozwala lepiej zarządzać pamięcią
krotka = tuple(lista_copy)
print(krotka)  # ('Radek', 'Tomek', 'Zenek', 'Marek')
print(type(krotka))  # <class 'tuple'>

krotka_liczby = 6, 7, 9, 2, 200
print(type(krotka_liczby))  # <class 'tuple'>

krotka_jeden = "Radek",
print(type(krotka_jeden))
# PEP* zaleca tworzenie krotki jednoelementowej z nawiasami
krotka_jeden = ("Radek",)
print(type(krotka_jeden))

print(krotka_liczby.index(9))
print(krotka_liczby.count(9))

# krotka_liczby[0] = 7  # TypeError: 'tuple' object does not support item assignment

# rozpakowanie krotki
a, b = 1, 2
a, *b = krotka_liczby  # * worek na pozostałe dane
print(a, b)  # 6 [7, 9, 2, 200]
a, b, *c = krotka_liczby
print(a, b, c)  # 6 7 [9, 2, 200]

# set (zbior) - przechowuje unikalne wartosci, nie posiada indeksu
# nie zachowuje kolejnosći podczas dodawania elementów
lista = [44, 55, 66, 77, 33, 31, 33, 55, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 11, 44, 77, 55, 31}
zbior.add(18)
zbior.add(18)
zbior.add(45)
zbior.add(33)
zbior.add(33)
zbior.add(54)
print(zbior)  # {33, 66, 11, 44, 77, 45, 18, 54, 55, 31}

pusty_zbior = set()
print(pusty_zbior)  # set()

zbior2 = {66, 11, 44, 55, 62, 999, 999}
print(zbior2)  # {66, 55, 999, 11, 44, 62}

# suma zbioró
print(zbior | zbior2)  # {33, 66, 999, 11, 44, 77, 45, 18, 54, 55, 62, 31}
print(zbior.union(zbior2))  # {33, 66, 999, 11, 44, 77, 45, 18, 54, 55, 62, 31}

# funkcja wewnętrzna
# dekoratory - funkcja, która jako argument przyjmuje inną funkcję
# dekoratory wykorzystują zasady funkci wewnętrznej
def fun1():
    print("To jest fun")

    def fun2():  # fun2 będzie zawierał adres funkcji fun2
        print("To jest fun2")

    return fun2  # zwracamy adres funkcji


def pliki(zadanie):
    print("Sprawdzam czy plik istnieje")

    def zapis():
        print("Zapisałem do pliku")

    def odczyt():
        print("Odczytałem z pliku")

    if zadanie == "zapis":
        return zapis
    else:
        return odczyt


fun1()
wynik = fun1()
print(wynik)  # <function fun1.<locals>.fun2 at 0x000001870AC78C20>
print(type(wynik))  # <class 'function'>
wynik()  # uruchomienie funkcji zawartej w zmiennej wynik

odczyt = pliki("odczyt")
odczyt()
# Sprawdzam czy plik istnieje
# Odczytałem z pliku

zapis = pliki("zapis")
zapis()
# Sprawdzam czy plik istnieje
# Zapisałem do pliku

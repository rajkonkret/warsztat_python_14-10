# dekorator - funkcja, którą przyjmuje inną funkcję, opakowuje nową funkcjonalnością
# dekoratory wykorzystują zasadę funkcji wewnętrznej, zagnieżdżonej
def dekor(func, a):
    def wew():
        print("Funkcja wewnętrzna jako dekorator")
        return func()

    return wew  # zwracamy adres funkcji wew


@dekor
def nasza_funkcja():
    print("funkcja, którą chcemy udekorować")


nasza_funkcja()
# funkcja, którą chcemy udekorować - tak działa bez dekoratora

# działanie z dekoratorem
# Funkcja wewnętrzna jako dekorator
# funkcja, którą chcemy udekorować

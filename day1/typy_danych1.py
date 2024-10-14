import sys

print("Nazywam się Radek")
print(type("Radek"))  # <class 'str'>
print(39)  # 39
print(type(39))  # <class 'int'>
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)
print(type("93"))  # <class 'str'>
# silne typowanie - nie zamienia typów sam
# print("93" + 45)  # TypeError: can only concatenate str (not "int") to str
print("93" + str(45))  # 9345, konkatenacja, łączenie, str() - rzutowanie na string
print(int("93") + 45)  # 138, int() - rzutowanie na int - liczby całkowite
print(5 * "93")  # 9393939393
print(5 * 93)  # 465

# zmienna - pudełko, przechowuje jedną wartość
name = "Radek"
print(name)
print(type(name))  # <class 'str'>
name: str = "Tomek"  # to jest tylko podpowiedź typu!
name = 90
print(name)
print(type(name))
# <class 'str'>
# 90
# <class 'int'>
# typowanie dynamiczne - mozna w każdej chwili wrzucic inny typ danych do zmiennej
# przyjmie ty wg tej wartości

wiek = 45
rok = 2023
temp = 36.6
print(type(temp))  # <class 'float'>, liczby zmiennoprzecinkowe
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308,
#                min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16,
#                radix=2, rounds=1)
print(0.1 + 0.5)  # 0.6
print(0.1 + 0.7)  # 0.7999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
# bład zaokraglenia - typy float
# decimal - pozwala ominąc problem zaokrąglenia

print(wiek + rok)  # 2068
print(wiek - rok)  # -1978
print(wiek / rok)  # 0.022244191794364803
print(wiek * rok)  # 91035
print(rok // wiek)  # 44, czesc całkowita z dzielenia
print(rok % wiek)  # modulo, reszta z dzielenia, 43
# ctrl alt l
print(wiek ** rok)
print(len(str(wiek ** rok)))  # 3345

print(54 - 5 * 43 / 2 + 4 / 2)
print(54 - (5 * 43) / 2 + 4 / 2)
print(54 - (5 * 43) / (2 + 4) / 2)
# ctrl d - kopiowanie linii
# -51.5
# -51.5
# 36.08333333333333

wersja = 3.900001
# f-string, formatowanie tekstu
# pozwala wstrzywkiwac wartości zmiennych w klamerki do ciagu tekstowego
print(f"Używamy wersji pythona {wersja}")
# Używamy wersji pythona 3.900001

# zaokrągla liczbę przy ywświetlaniu do miejsca po przecinku
print(f"Używamy wersji pythona {wersja:.1f}")
print(f"Używamy wersji pythona {wersja:.2f}")
# Używamy wersji pythona 3.9
# Używamy wersji pythona 3.90
print("Wersja", wersja)  # Wersja 3.900001

print("Używamy %f" % wersja)  # %f - float, weryfikuje typ, Używamy 3.900001
print("Używamy wersji {}".format(wersja))  # Używamy wersji 3.900001
print(f"""Tekst wielolinijkowy
{wersja}
""")
# "Tekst wielolinijkowy
# 3.900001"

# teksty są niemutowalne
imie = "Radek Radek"
imie.upper()
print(imie)  # Radek Radek
""" Return a copy of the string converted to uppercase. """
print(imie.upper())
wynik = imie.upper()
print(wynik)
# Radek Radek
# RADEK RADEK
# RADEK RADEK

liczba = 456234789123
# print(liczba.upper())  # AttributeError: 'int' object has no attribute 'upper'
print(liczba)  # 456234789123
print(f"Nasza duza liczba {liczba:,}")
print(f"Nasza duza liczba {liczba:_}")
# Nasza duza lizba 456,234,789,123
# Nasza duza lizba 456_234_789_123
print(f"Nasza duza liczba {liczba:_}".replace("_", " "))  # Nasza duza liczba 456 234 789 123

liczba2 = 150000000000
liczba2 = 150_000_000_000
print(type(liczba2))  # <class 'int'>
print(liczba2)  # 150000000000
liczba3 = 10_0000_000
print(liczba3)  # 100000000

# typ logiczny
# True, False -> prawda, fałsz
czy_znasz_python = True
print(czy_znasz_python)  # True
print(type(czy_znasz_python))  # <class 'bool'>

# 1, 0
print(int(True))  # 1
print(int(False))  # 0

print(bool(1))
print(bool(0))
# True
# False
print(bool(100))  # True
print(bool(-10))  # True
print(bool("radek"))  # True

print(bool(""))
print(bool(None))
# None  - null - nic, stan nieokreslony

tekst = "    Tekst    "
print(tekst.strip())  # "Tekst" - czyszczenie z biąlych znków (spacji) wiodących i końcowych

tekst2 = "Radek"
print(f"{tekst2:>10}")  # "     Radek"
print(f"{tekst2:<12}")  # "Radek       "
print(f"{tekst2:^12}")  # "   Radek    "

a = 10
print(f"Zmienna a  = {a}")
print(f"Zmienna {a=}")
# Zmienna a  = 10
# Zmienna a=10

tekst_x = "Witaj Świecie"
print(tekst_x.lower())  # "witaj świecie"
print(tekst_x.upper())  # "WITAJ ŚWIECIE"
print(tekst_x.capitalize())  # "Witaj świecie"

encode_s = tekst_x.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie' typ bajtowy
# \xc5\x9a - wartość szesnastkowa bajtów

print(encode_s.decode('utf-8'))  # Witaj Świecie

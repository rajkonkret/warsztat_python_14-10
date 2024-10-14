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

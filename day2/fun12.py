# napisac funkcję, która przyjmuje argumenty age, first, last
# age powinien miec ustawioną wartośc domyśłną
# z tych argumentów funkcja zbuduje słownik
# należy pobierać argumenty w pętli while
# zastosowac "klawisz ucieczki"


def build_dict(first, last, age=None):
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age

    return person


while True:
    print("Podaj imię i nazwisko")
    print("Wpisz q by wyjsć")

    f_name = input("Podaj imię")
    if f_name == 'q':
        break

    l_name = input("Podaj nazwisko")
    if l_name == 'q':
        break

    age = input("Podaj wiek")
    if age == 'q':
        break

    print(build_dict(f_name, l_name, age))
# {'first': 'radek', 'last': 'kowalski', 'age': '67'}
# {'first': 'radek', 'last': 'maluch'}
# Podaj imię i nazwisko
# Wpisz q by wyjsć
# Podaj imięq
#
# Process finished with exit code 0

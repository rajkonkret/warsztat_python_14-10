# __missing__ - wykonywana gdy brak klucza w słowniku
class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


class AutoKeyDict(dict):
    def __missing__(self, key):
        self[key] = 0
        return key


class CaseInsenstiveDict(dict):
    def __missing__(self, key):
        return self.get(key.lower())


d_python = {}
# print(d_python['name'])  # KeyError: 'name'

d1 = DefaultDict()
print(type(d1))  # <class '__main__.DefaultDict'>
print(d1)  # {}
print(d1['name'])  # w miejsce KeyError mamy wartośc domyślną default

# zrobic słownik tak by dla danego klucza wstawiała wartośc 0
a1 = AutoKeyDict()
print(a1)
print(a1['name'])
print(a1)
# {}
# name
# {'name': 0}

# niezaleznie czy duzymi czy malymi podamy klucz zawsze ma szukac klucza w słowniku małymi literami
csd = CaseInsenstiveDict()
csd['name'] = "Radek"
print(csd['Name'])  # Radek

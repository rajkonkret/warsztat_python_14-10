# odczytac dane z pliku dane.pickle i wyświetlic w czytelnej dla człowieka formie
import pickle
from dataclasses import dataclass
from kl15 import Person

# @dataclass
# class Person:
#     first_name: str
#     last_name: str
#     id: int

with open('dane.pickle', "rb") as file:
    p = pickle.load(
        file)  # [Person(first_name='Jan', last_name='Kowalski', id=1), Person(first_name='Maciej', last_name='Nowak', id=2)]

print(p)  # [Person(first_name='Jan', last_name='Kowalski', id=1), Person(first_name='Maciej', last_name='Nowak', id=2)]

for person in p:
    person.greets()

# [Person(first_name='Jan', last_name='Kowalski', id=1), Person(first_name='Maciej', last_name='Nowak', id=2)]
# My name is Jan
# My name is Maciej

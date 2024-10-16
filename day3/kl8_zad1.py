# stworzenie ksiazki telefonicznej z wykorzystanie petli while True
# dodaj kontakt, usun kontakt, wyszukaj kontakt, wyswietl kontakt

# -----------
# stworzyc system zarzadzania biblioteką klasa Book
# dodnie ksiazki, wypozyczenie ksiazki, zwracanie ksiązki
# obsłużyc błedy
# Dodac Library i usera
contacts = {}  # słownik
while True:
    print(f"""
    1. Dodaj kontakt
    2. Usuń kontakt
    3. Wyszukaj kontakt
    4. Wyświetl kontakty
    5. Koniec
""")
    try:
        odp = input("Wybierz opcję")
        if odp == "1":
            name = input("Podaj imię kontaktu")
            number = input("Podaj numer telefonu (tylko cyfry)")
            if not number.isdigit():
                raise ValueError("Numer telefonu powinien zawierać cyfry")  # rzucenie wyjątku
            else:
                contacts[name.lower()] = number
                print("Kontakt został dopisany")
        elif odp == "2":
            name = input("Podaj imię kontaktu do usunięcia")
            if name.lower() in contacts:
                # del contacts[name.lower()]
                contacts.pop(name.lower())
                print(f"Kontakt {name} został usunięty")
            else:
                print(f"Nie znaleziono kontaktu o imieniu {name}")
        elif odp == "3":
            name = input("Podaj imię do wyszukania")
            if name.lower() in contacts:
                print(f"Kontakt {name.capitalize()} nr telefonu {contacts[name.lower()]}")
            else:
                print(f"Nie znaleziono kontaktu o imieniu {name}")
        elif odp == "4":
            print(f"Lista konatktów {contacts}")
        elif odp == "5":
            break
        else:
            print("Błędny wybór")
    except Exception as e:
        print("Bład", e)

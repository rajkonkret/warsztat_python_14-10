# -----------
# stworzyc system zarzadzania biblioteką klasa Book
# dodnie ksiazki, wypozyczenie ksiazki, zwracanie ksiązki
# obsłużyc błedy
# Dodac Library i usera

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"'Author: {self.author!r}, Tytuł: {self.title!r}, ISBN: {self.isbn!r}"


# book = Book("Pan Tadeusz", "Adam Mickiewicz", "A1234567890")
# print(book) # 'Author: 'Adam Mickiewicz', Tytuł: 'Pan Tadeusz', ISBN: 'A1234567890'
class Library:
    def __init__(self):
        self.dostepne_ksiazki = []
        self.wypozyczone_ksiazki = []

    def fun_dodaj_ksiazke(self, book: "Book"):
        self.dostepne_ksiazki.append(book)

    def fun_ksiazki_do_wypozyczenia(self):
        return self.dostepne_ksiazki

    def fun_wypozycz_ksiazke(self, isbn):
        for book in self.dostepne_ksiazki:
            if book.isbn == isbn:
                self.dostepne_ksiazki.remove(book)
                self.wypozyczone_ksiazki.append(book)
                return book
        raise Exception("Nie ma takiej ksiązki")

    def fun_wypozyczone_ksiazki(self):
        return self.wypozyczone_ksiazki

    def fun_zwroc_ksiazke(self, isbn):
        for book in self.wypozyczone_ksiazki:
            if book.isbn == isbn:
                self.dostepne_ksiazki.append(book)
                self.wypozyczone_ksiazki.remove(book)
                return True
        raise Exception("Ksiazka nie z naszej biblioteki")


biblioteka = Library()
while True:
    print(f"""
    1. Dodaj ksiązkę
    2. Wypożycz ksiązkę
    3. Pokaż dostępne
    4. Pokaż wypożyczone
    5. Zwróć ksiazkę
    6. Koninec
""")
    try:
        odp = input("Wybierz opcję")
        if odp == "1":
            author = input("Podaj autora")
            title = input("Podaj tytuł")
            isbn = input("Podaj numer ISBN")
            biblioteka.fun_dodaj_ksiazke(Book(title, author, isbn))
            print(f"Ksiązka została dodana")
        elif odp == "2":
            isbn = input("Podaj ISBN ksiązki, którą chesz wypożyczyc")
            book = biblioteka.fun_wypozycz_ksiazke(isbn)
            print(f"Ksiązka została wypożyczona")
        elif odp == "3":
            print(f"Dostępne ksiązki {biblioteka.fun_ksiazki_do_wypozyczenia()}")
        elif odp == "4":
            print(f"Wypożyczone ksiązki {biblioteka.fun_wypozyczone_ksiazki()}")
        elif odp == "5":
            isbn = input("Podaj ISBN ksiązki, którą chesz zwrócić")
            book = biblioteka.fun_zwroc_ksiazke(isbn)
            if book:
                print("Ksiązka zostałą zwrócona")
        elif odp == "6":
            break
        else:
            print("Błędny wybór")
    except Exception as e:
        print("Bład", e)

# Wybierz opcję3
# Dostępne ksiązki ['Author: 'mickiewicz', Tytuł: 'pan tadeusz', ISBN: '123456789', 'Author: '', Tytuł: '', ISBN: '']

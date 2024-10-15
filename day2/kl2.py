class Contact:
    all_contacts = []  # pusta lista, wspolna dla wszystkich obiektów klasy

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):  # repr nadpisuje tez __str__ gdy wyraźnie nie nadpisaliśmy
        return f"{self.name} {self.email}"


class Suplier(Contact):
    """
    Klasa dziedziczy po klasie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


c1 = Contact("Adam", "admin@wp.pl")
print(c1)  # Adam admin@wp.pl
c2 = Contact("Radek", "radek@wp.pl")
c3 = Contact("Tomek", "tomek@wp.pl")
print(c1.all_contacts)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
print(c3.all_contacts)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
s1 = Suplier("Marek", "marek@onet.pl")
print(s1.all_contacts)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@onet.pl]
s1.order("kawa")  # kawa zamówiono od Marek

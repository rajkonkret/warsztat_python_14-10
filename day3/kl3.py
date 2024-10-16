from pprint import pprint


class ContactList(list["Contact"]):
    def search(self, name):
        matching_contact = []
        for c in self:
            if name in c.name:
                matching_contact.append(c)
        return matching_contact


class Contact:
    all_contacts = ContactList()  # pusta lista, wspolna dla wszystkich obiektów klasy

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


class Friend(Suplier):
    """
    Klasa dziedziczy po Suplier
    """

    def __init__(self, name, email, phone='00000000'):
        super().__init__(name, email)  # super() - musimy użyć konstruktor z klasy wyższej
        self.phone = phone

    def __repr__(self):  # repr nadpisuje tez __str__ gdy wyraźnie nie nadpisaliśmy
        return f"{self.name!r} {self.email!r}, +48{self.phone!r}"


lista = []
# lista.search()  # AttributeError: 'list' object has no attribute 'search'
lista_contact = ContactList()
print(lista_contact.search("radek"))  # []
c1 = Contact("Adam", "admin@wp.pl")
print(c1)  # Adam admin@wp.pl
c2 = Contact("Radek", "radek@wp.pl")
c3 = Contact("Tomek", "tomek@wp.pl")
print(c1.all_contacts)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
print(c3.all_contacts)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
# Adam admin@wp.pl
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
print(c1.all_contacts.search("Radek"))  # [Radek radek@wp.pl]
s1 = Suplier("Marek", "marek@onet.pl")
print(s1.all_contacts)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@onet.pl]
s1.order("kawa")  # kawa zamówiono od Marek
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@onet.pl]
# kawa zamówiono od Marek
f1 = Friend("Kasia", 'kasia@wp.pl')
print(f1)  # Kasia kasia@wp.pl, +4800000000 -> po dodaniu !r -> 'Kasia' 'kasia@wp.pl', +48'00000000'
f1.order("herbata")  # herbata zamówiono od Kasia
print(f1.all_contacts)
# [Adam admin @ wp.pl, Radek radek @ wp.pl,
#  Tomek tomek @ wp.pl, Marek marek @ onet.pl,
#  Kasia kasia @ wp.pl, +4800000000]
f2 = Friend("Zenek", "zenek@bialystok.pl", '678980123')
print(f2)  # Zenek zenek@bialystok.pl, +48678980123
print(f2.all_contacts)
# [Adam admin@wp.pl,
#  Radek radek@wp.pl,
#  Tomek tomek@wp.pl,
#  Marek marek@onet.pl,
#  Kasia kasia@wp.pl, +4800000000,
#  Zenek zenek@bialystok.pl, +48678980123]
print(Friend.__mro__)
# (<class '__main__.Friend'>, <class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>)
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@onet.pl, 'Kasia' 'kasia@wp.pl', +48'00000000', 'Zenek' 'zenek@bialystok.pl', +48'678980123']
pprint(f1.all_contacts)
# [Adam admin@wp.pl,
#  Radek radek@wp.pl,
#  Tomek tomek@wp.pl,
#  Marek marek@onet.pl,
#  'Kasia' 'kasia@wp.pl', +48'00000000',
#  'Zenek' 'zenek@bialystok.pl', +48'678980123']

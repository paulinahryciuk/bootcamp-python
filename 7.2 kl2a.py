class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return f"{self.name} {self.email}"


class Suplier(Contact):
    """
    dziedziczy
    """

    def order(self, order):
        print(f"{order} zamowiona przez {self.name}")


c1 = Contact("Adam", "adam@wp.pl")
c2 = Contact("Radek", "radek@wp.pl")
c3 = Contact("Tomek", "tomek@wp.pl")
print(c1.all_contacts)

s1 = Suplier("Marek", "marek@wp.pl")
print(c1.all_contacts)
print(s1.all_contacts)
s1.order("herbata")

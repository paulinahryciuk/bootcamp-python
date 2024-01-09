#Biblioteka

class Library:
    """
    Klasa opisujaca zasob biblioteki
    """

    def __init__(self, resource):
        self.resource = resource


    def show_resources(self):
        print(f"Aktualny zasob biblioteki: \n{self.resource}")


class Book(Library):
    """
    Klasa opisujaca ksiazki
    """
    def __init__(self, resource, title):
        super().__init__(resource)
        self.title = title

    def show_status(self):
        if self.title in self.resource:
            print(f"Ksiazka {self.title} jest dostepna do wypozyczenia")
        else:
            print(f"Ksiazka {self.title} jest aktualnie wypozyczona")

    def adding_book(self):
        return self.resource.append(self.title)


class User(Book):
    """
    Klasa opisujaca uzytkownika biblioteki
    """

    def __init__(self, resource, title, account):
        super().__init__(resource, title)
        self.account = account

    def show_account(self):
        print(f"Uzytkownik na swoim koncie ma wypozyczone pozycje: {self.account}")

    def borrowing(self):
        return self.account.append(self.title)
        return self.resource.remove(self.title)

    def ret_book(self):
        return self.account.remove(self.title)
        return self.resource.append(self.title)

u1 = User(["Potop", "Nad Niemnem", "Lalka", "Romeo i Julia"],"Lalka",["AAA"])
u1.show_account()
u1.borrowing()
u1.show_account()
u1.ret_book()
u1.show_account()
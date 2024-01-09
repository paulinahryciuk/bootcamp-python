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

    def adding_book(self, title):
        return self.resource.append(title)


class User(Library):
    """
    Klasa opisujaca uzytkownika biblioteki
    """

    def __init__(self, resource, account):
        super().__init__(resource)
        self.account = account

    def show_account(self):
        print(f"Uzytkownik na swoim koncie ma wypozyczone pozycje: {self.account}")

    def borrowing(self, title):
        return self.account.append(title)
        return self.resource.remove(title)

    def ret_book(self, title):
        return self.account.remove(title)
        return self.resource.append(title)

bibl_resource = ["Potop", "Nad Niemnem", "Lalka", "Romeo i Julia"]
user1_account = ["Basnie", "Mity"]
user1 = User(bibl_resource, user1_account)
ks1 = Book(bibl_resource,"A")

print("Witamy w bibliotece!")
while True:
    print("1. Chce wypozyczyc ksiazke\n2. Chce oddac ksiazke\n3. Chce podarowac ksiazke dla biblioteki\n4. Koniec")
    task = input("Wybieram: ")
    if task==str(1):
        book_user = input("Jaka ksiazke chcesz wypozyczyc? ")
        user1.borrowing(book_user)
        print("Podsumowanie:")
        user1.show_account()
    elif task == str(2):
        book_return = input("Jaka ksiazke oddajesz? ")
        user1.ret_book(book_return)
        print("Podsumowanie:")
        user1.show_account()
    elif task==str(3):
        book_gift = input("Jaka ksiazke chcesz dodac do zasobu? ")
        ks1.adding_book(book_gift)
        ks1.show_resources()
    elif task == "4":
        print ("Do zobaczenia!")
        break
    else:
        print("Sprobuj jeszcze raz, wybrales zly numer")
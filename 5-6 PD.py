#Biblioteka

resource = ["Potop", "Nad Niemnem", "Lalka", "Romeo i Julia"]
status = []
class Book:
    """
    Klasa opisujaca ksiazki
    """
    def __init__(self,title):
        self.title = title


class Library(Book):
    """
    Klasa opisujaca zasob biblioteki
    """

    def __init__(self, title, resource):
        super().__init__(title)
        self.resource = resource


    def adding_book(self,title):
        return resource.append(self.title)

    def show_resources(self):
        return self.resource

class User(Book):
    """
    Klasa opisujaca uzytkownika biblioteki
    """


    def __init__(self,title, name,status):
        super().__init__(title)
        self.name = name
        self.status = status


    def show_status(self):
        print(f"Uzytkownik {self.name} na swoim koncie ma wypozyczone pozycje: {self.status}")


    def borrowing (self,title):
        return self.status.append(self.title)
        return resource.remove(self.title)


    def ret_book (self,title):
        return self.status.remove(self.title)
        return resource.append(self.title)

book1 = Book("Dzuma")
book2 = Book("Potop")
biblioteka = Library(book1,resource)
user1 = User(book2,"Ada",status)

biblioteka.adding_book("dzuma")
print(biblioteka.show_resources())
user1.borrowing(book2)
print(user1.show_status())
print(biblioteka.show_resources())

print("Witamy w bibliotece!")
while True:
    print("1. Chce wypozyczyc ksiazke\n2. Chce oddac ksiazke\n3. Chce podarowac skiazke dla biblioteki\n4. Koniec")
    task = input("Wybieram: ")
    if task==str(1):
        book_user = input("Jaka ksiazke chcesz wypozyczyc? ")
        user1.borrowing(book_user)
        print(user1.show_status)
    elif task == str(2):
        book_return = input("Jaka ksiazke oddajesz? ")
        user1.ret_book(book_return)
        print(user1.show_status())
    elif task==str(3):
        book_gift = input("Jaka ksiazke chcesz dodac do zasobu? ")
        biblioteka.adding_book(book_gift)
        print(biblioteka.show_resources())
    elif task == "4":
        break
    else:
        print("Sprobuj jeszcze raz, wybrales zly numer")
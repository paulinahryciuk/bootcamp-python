class PrintMedia:
    def print_media(self):
        print("Drukowana tresc")


class Digitalmedia:
    def digital_media(self):
        print("Cyfrowa tresc")


class Book(PrintMedia):
    pass

class Ebook(Digitalmedia):
    pass

class MultimediaBook(Book, Ebook):
    pass

multimedia_ebook = MultimediaBook()
print(MultimediaBook.__mro__)
multimedia_ebook.print_media()
multimedia_ebook.digital_media()
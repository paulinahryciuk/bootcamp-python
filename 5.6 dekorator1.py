def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()

    return wew

@dekor
def hej():
    print("Hej!!")

hej()

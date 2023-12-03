def rastauracja(typ_zamowienia):
    print(("witamy"))

    def zamow_pizze():
        print("pizza zamwoiona")

    def zamow_napoj ():
        print("zamow napoj")

    if typ_zamowienia =="napoj":
        return  zamow_napoj
    else:
        return  zamow_pizze

    zamowienie_napoj = rastauracja("napoj")
    zamowienie_napoj()
    zamowienie_napoj('cola')
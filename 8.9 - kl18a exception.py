class MyException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


# print(2/0)
# raise  ZeroDivisionError("Nie dziel przez zero")

try:
    x = int(input("podaj liczbe calk"))
    if x<0:
        print("Liczba ma byc wieksza od zero")
        raise MyException("Liczba musi bc dodatnia")
except MyException:
    print("wystapil wyjatek Myexc")
except ValueError:
    print("wys bl vwart")
else:
    print("popor wart")
finally:
    print("zakon dzialania")

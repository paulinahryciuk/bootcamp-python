# odp = True
# if odp:
#     print("brawo")
# if True:
#     pass
#
# podatek = 0.9
# zarobki = float(input("podaj dochod"))
# if zarobki<10000:
#     podatek = 0.0
# elif zarobki <10000:
#     podatek = 0.4
# elif zarobki>=100000 and zarobki<29999:
#     podatek=0.2
# else:
#     podatek = 0.9
# print((f"placisz {zarobki* podatek} podatku"))

# suma_zam = 200
# if suma_zam>150:
#     rabacik = 25
# else:
#     rabacik = 0
# print(f"rabacik to {rabacik}")
#
# rabat = 25 if suma_zam>150 else 0
# print(f"rabacik to {rabacik}")

#
# logi = ["console", "email", "inny"]
# import random
#
# log = random.choice(logi)
# if log == "console":
#     print("critical")
# elif log == "email":
#     print("medium")
# else:
#     print("inne")
#
# punkty = 0
# pytanie1 = int(input("ile to jest 1 + 1 "))
# pytanie2 = int(input("ile to jest 2 + 2 "))
# pytanie3 = int(input("ile to jest 3 + 3 "))
# if pytanie1 == 2:
#     print("good job")
#     punkty += 1
# else:
#     print("zla odpowiedz")
# if pytanie2 == 4:
#     print("good job")
#     punkty += 1
# else:
#     print("zla odpowiedz")
# if pytanie3 == 6:
#     print("good job")
#     punkty += 1
# else:
#     print("zla odpowiedz")
# print(f"uzyskales {punkty} punktow")

lang = input("jezyk")
match lang:
    case "python":
        print("lubie pythona")
    case "java":
        print("java to kawa")
    case _:
        print("nie znam takiego")

dane = ''
match dane:
    case [a,b,c]:
        print(f"lista z 3 elementami ")
    case {"nazwa":n, "wiek": w}:
        print(f"slownik reprezentujacy {n} osobe")
    case _:
        print("inne")



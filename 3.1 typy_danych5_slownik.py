# my_dict = {"A": "one", "B":"two","C":"Three","D":"four"}
# print(my_dict)
# print(type(my_dict))
#
# empty_dict = dict()
# print(empty_dict)
#
# dict_with_integer = {1:"one", 2:"two", 3:"three"}
# print(dict_with_integer)
#
# dict_with_integer2 = dict({1:"one", 2:"two", 3:"three"})
# print(dict_with_integer2)
#
# dict_mixed = {1:"one", "A":"two", 3:"three"}
# print(dict_mixed)
#
# print(dict_mixed.keys())
# print(my_dict.keys())
# print(dict_with_integer.keys())
# print(dict_with_integer2.keys())
# print(dict_mixed.items())
# print(dict_mixed.values())
# dict_with_list = {1:'one', 2:'two', 'A' :['asif', "jhon","maria"]}
# print(dict_with_list)
# dict_with_list2 = {1:'one', 2:'two', 'A' :('asif', "jhon","maria")}
# print(dict_with_list2)
# dict_with_list2 = {1:'one',
#                    2:'two',
#                    'A' :{'asif', "jhon","maria"}}
# print(dict_with_list2)
# dict_with_list3 = {1:'one',
#                    2:'two',
#                    'A' :{'asif', "jhon","maria"},
#                     'B' :{'name': 'asif', "jhon":"maria"}}
# print(dict_with_list3)
#
# keys = {'a','b','c','d'}
# my_dict2 = dict.fromkeys(keys)
# print(my_dict2)
# value = 10
# my_dict3 = dict.fromkeys(keys,value)
# print(my_dict3)
#
# print(my_dict["A"])
# print(my_dict3['d'])
# print(dict_with_list3["B"])
# print(dict_with_list2["A"])
#
# print(my_dict3.get("A"))
# print(my_dict3.get("F","nie ma"))
#
# my_dict5 = {'Name':"Radek", "ID":12345, "DOB":1991, "Adress":"Warsaw"}
# print(my_dict5)
#
# my_dict5["DOB"] = '1980'
# print(my_dict5)
# my_dict5["Adress"]= "Krakow"
# print(my_dict5)
# dict1 = {"DOB":"1995"}
# print(dict1)
#
# my_dict5.update((dict1))
# print((my_dict5))
#
# my_dict5['job']="developer"
# dict2 = {"cpi":3.4}
# my_dict5.update(dict2)
# print(my_dict5)
#
# print(my_dict5.pop("cpi"))
# print(my_dict5)
#
# my_dict5 = {'Name':"Radek", "ID":12345, "DOB":1991, "Adress":"Warsaw"}
# my_dict_copy_reference = my_dict5
# my_dict_copy.copy()

# dict_ang = {"jablko": "apple", "banan": "banana", "cytryna": "lemon"}
# print(dict_ang.keys())
# slowo = input("Podaj slowo: ")
# print((dict_ang.get(slowo.lower().replace(' ','', "podaj inne")))

a = int(input("podaj liczbe: "))
b = int(input("podaj liczbe: "))
print(f"wynik dodawania: {a + b}")

my_dict = {"A": "one", "B":"two","C":"Three","D":"four"}
print(my_dict)
print(type(my_dict))

empty_dict = dict()
print(empty_dict)

dict_with_integer = {1:"one", 2:"two", 3:"three"}
print(dict_with_integer)

dict_with_integer2 = dict({1:"one", 2:"two", 3:"three"})
print(dict_with_integer2)

dict_mixed = {1:"one", "A":"two", 3:"three"}
print(dict_mixed)

print(dict_mixed.keys())
print(my_dict.keys())
print(dict_with_integer.keys())
print(dict_with_integer2.keys())
print(dict_mixed.items())
print(dict_mixed.values())
dict_with_list = {1:'one', 2:'two', 'A' :['asif', "jhon","maria"]}
print(dict_with_list)
dict_with_list2 = {1:'one', 2:'two', 'A' :('asif', "jhon","maria")}
print(dict_with_list2)
dict_with_list2 = {1:'one',
                   2:'two',
                   'A' :{'asif', "jhon","maria"}}
print(dict_with_list2)
dict_with_list3 = {1:'one',
                   2:'two',
                   'A' :{'asif', "jhon","maria"},
                    'B' :{'name': 'asif', "jhon":"maria"}}
print(dict_with_list3)
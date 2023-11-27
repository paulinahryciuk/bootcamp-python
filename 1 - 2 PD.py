# 1
fruits = ["jablko", "banan", "kiwi", "gruszka", "arbuz"]

# 2
print(fruits[1])

# 3
fruits[2] = "malina"

# 4
colors = ("bialy", "czarny", "czerwony")

# 5
print(colors[-1])

# 8
me = "Paulina Hryciuk"
other_string = "Jan Kowalski"

# 9
name_surname = other_string.split()
name = name_surname[0]
surname = name_surname[1]

# 10
print(f"Mam na imie {name} i mam 25 lat")

# 1
list = [1, 2, 3, 4, 5]
print(len(list))

# 2
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = list_1 + list_2
print(list_3)

# 3
list_3.append(4)
print(list_3)

# 4
krotka = (1, 2, 3, 4, 5)
print(krotka[2])

# 5
list_reverse = list.copy()
list_reverse.sort(reverse = True)
print(list_reverse)

#6
maximum = max(list)
print(maximum)

#7
text_1 = "Python"
text_2 = "jest super!"
text_3 = text_1 + " " + text_2
print(text_3)

#8
text_4 = "Lubie Pythona"
text_5 = text_4.replace("Pythona","programowanie")
print((text_5))

#9
text_4 = "Lubie Pythona"
space = text_4.index(' ')
new_text = text_4[(space+1):-1]
print((new_text))

#10
nieparzyste = [1,3,5,7,9]
print(nieparzyste)

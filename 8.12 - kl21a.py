class MyNumber:
    def __init__(self, value):
        self.value = value

num1 = MyNumber(5)
num2 = MyNumber(15)
print(5<15)
# print(num1<num2)

class MyNumber2:
    def __init__(self,value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

num3 = MyNumber2(5)
num4 = MyNumber2(15)
print(num3<num4)
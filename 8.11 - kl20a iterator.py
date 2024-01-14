lista = [1,2,3,4,5]
for i in lista:
    print(i)

iterator = iter(lista)
print(iterator)
print(type(iterator))

print(next(iterator))
print('zrob cos')
print(next(iterator))


class Count:
    def __init__(self, low, high):
        self.current =low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise  StopIteration
        else:
            self.current +=1
            return self.current -1

counter = Count(1,5)
while True:
    try:
        number = next(counter)
        print(number)
    except StopIteration:
        break
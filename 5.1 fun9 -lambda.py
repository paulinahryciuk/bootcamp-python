odejmij = lambda a,b :a-b
print(odejmij(6,8))

addition = lambda a,b:a+b
print(addition(6,7))
res = addition(6,7)
print(f"wynik{res}")

res = lambda *args: sum(args)
print(res(10,20))

res = lambda ** kwargs: sum(kwargs.values())
print(res(a=10, b=20))

produce = lambda a,b:a*b

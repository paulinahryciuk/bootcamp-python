def fun1():
    print("to jest fun1")

    def fun2():
        print(("to jest fun2"))


    return fun2

fun1()
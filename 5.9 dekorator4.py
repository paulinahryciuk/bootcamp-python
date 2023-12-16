def install_decorator(func):
    def wrapper():
        print("pleas accept")
        func()
    return wrapper

def install_decorator2(func):
    def wrapper():
        print("please enter key")
        func()
    return wrapper

@install_decorator
def install_linux():
    print("linux..sterded \n")


@install_decorator
def install_windows():
    print("windows..sterded \n")


@install_decorator2
@install_decorator
def install_mac():
    print(("mac..sterded \n"))

install_windows()
install_linux()
print(("--------------"))
install_mac()
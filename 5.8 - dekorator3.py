def sub_decorator(func):
    def wrapper(num1, num2):
        if num1<num2:
            num1, num2 = num2, num1
            return func(num1,num2)

    return wrapper
@sub_decorator
def substract(num1, num2):
    res= num1 - num2
    print("result is:", res)

substract(2,4)
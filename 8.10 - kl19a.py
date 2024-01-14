class MyError(Exception):
    def __init__(self,msg, err_code):
        super().__init__(msg)
        self.err_code = err_code
        
class MyValue(MyError):
    def __init__(self,msg):
        super().__init__(msg, err_code=100)
        
class MyTypeError(MyError):
    def __init__(self,msg):
        super().__init__(msg, err_code=200)

def my_function(x: int, y: int ):
    if not isinstance(x, int):
        raise MyTypeError('x must be integer')
    if not isinstance(y, int):
        raise MyTypeError('y must be integer')
    if y == 0:
        raise MyValueError('y cannot be zero')

    return x/y

try:
    result = my_function(4,0)
except MyTypeError as e :
    print("my type err", e)
    print("kod", e.err_code)
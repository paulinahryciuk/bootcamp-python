def add (a,b):
    return a+b

def test_addition():
    result = add(2,3)
    assert result == 5

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("dzielenie przez zero")

def test_dividion_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)

def test_dividion_1():
    assert divide(5,1)==5

def test_dividion_2():
    assert divide(6,2)==3
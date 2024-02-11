import  pytest

def caluclate_square(num):
    return num ** 2

def test_square_1():
    assert caluclate_square(2)==4


@pytest.mark.parametrize("input, excepted_output", [(2,4),(3,9,(4,16))])
def test_square_calc_parametrized(input, excepted_output):
    assert caluclate_square(input) == excepted_output

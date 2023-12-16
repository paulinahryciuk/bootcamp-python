import time
import numpy as np
# pip install numpy


def measure_time(func):
    def wrapper(*arg,**kwargs):
        start_time = time.time()
        result = func(*arg,**kwargs)
        end_time = time.time()
        excution_time = end_time - start_time
        print(f"czas wykon funk {func.__name__}:{excution_time}")
        return result
    return wrapper

@measure_time
def my_function():
    pass

my_function()

@measure_time
def my_for_sum():
    suma = 0
    for i in range(12_000_000):
        suma += i
    print("suma: ", sum)

@measure_time
def my_sum_without_for():
    total = sum(range(12_000_000))
    print("suma", total)

@measure_time
def my_sum_np():
    total = np.sum(np.arange(12_000_000),dtype=np.int64)
    print("suma", total)

my_sum_without_for()
my_sum_np()
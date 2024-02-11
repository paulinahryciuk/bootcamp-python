import random
import time
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

total_points_inside_circle = 0

def monte_carl_pi(n):
    points_ins = 0

    for _ in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        if x**2 + y**2 <=1:
            points_ins +=1

    return 4 * (points_ins / n)

def no_threads(iterations):
    start = time.time()
    pi = monte_carl_pi(interations)
    end = time.time()
    print(f"Bez watkow {pi}, czas {end - start}")
def with_processes(iteration):
    num_processes = 8
    iterations_per_process = itearations // num_processes

def with_threats(iterations):
    num_threads = 8
    iterations_per_thread = iterations // num_threads
    threds = []

    def thread_monte_carlo_pi():
        global = total_points_inside_circle
        points_inside_circle_2 = monte_carl_pi(iterations_per_thread)
        with lock:
            total_points_inside_circle += points_inside_circle_2

    lock = threading.Lock()
    start = time.time()
    for _ in range(num_threads):
        threds = threading.Thread(target= thread_monte_carlo_pi)
        threds.append(thread)
        threds.start()

    for thread in threads:
        thread.join()

    pi = 4*(total_points_inside_circe / num_threads*4)
    end = time.time()
    print(f"z watkami {pi} , czas {end - start}")


iterations(10_000_000)

if __name__ =='main__':
    no_threads(iterations)
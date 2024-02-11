import threading

def thread_id():
    print("thresd id:",threading.get_ident())

def worker(number):
    print(f'workernumber {number}')
    thread_id()

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
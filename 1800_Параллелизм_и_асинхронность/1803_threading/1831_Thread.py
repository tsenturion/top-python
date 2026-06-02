"""
1831_Thread
"""

import threading

def worker():
    print("Поток начал работу")
    print("Поток закончил работу")
    

#worker()
thread = threading.Thread(target=worker)
thread.start()
thread.join()
print("Главный поток завершен")



print()
def worker(name):
    print(f"Поток {name} начал работу")
    print(f"Поток {name} закончил работу")

thread = threading.Thread(target=worker, args=("Thread-1",))
thread.start()
thread.join()
print("Главный поток завершен")


print()
import time

def worker(number):
    print(f"Поток {number} начал работу")
    time.sleep(1)
    print(f"Поток {number} закончил работу")
    
    
threads = []

for i in range(5):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Главный поток завершен")

counter = 0

def worker():
    global counter
    for _ in range(100000):
        counter += 1
        
thread = threading.Thread(target=worker)
thread.start()
thread.join()
print(f"Значение счетчика: {counter}")
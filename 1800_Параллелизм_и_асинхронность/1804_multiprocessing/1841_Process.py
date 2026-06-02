"""
1841_Process
"""

from multiprocessing import Process

def worker():
    print("Процесс начал работу")
    print("Процесс закончил работу")
    
# process = Process(target=worker)
# process.start()
# process.join()

def worker(number):
    print(f"Процесс {number} начал работу")
    print(f"Процесс {number} закончил работу")
    
# if __name__ == '__main__':
#     process = Process(target=worker, args=(1,))
#     process.start()
#     process.join()

import time
def worker(number):
    print(f"Процесс {number} начал работу")
    time.sleep(1)
    print(f"Процесс {number} закончил работу")

# if __name__ == '__main__':    
#     processes = []

#     for i in range(5):
#         process = Process(target=worker, args=(i,))
#         processes.append(process)
#         process.start()
        
#     for process in processes:
#         process.join()
    
counter = 0
def worker():
    global counter
    for _ in range(100000):
        counter += 1
    print(f"Значение счетчика в процессе: {counter}")
        
        
if __name__ == '__main__':        
    process = Process(target=worker)
    process.start()
    process.join()
    print(f"Значение счетчика: {counter}")
    
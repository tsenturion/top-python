"""
1831_Thread
"""

import threading

def worker():
    print("Поток начал работу")
    print("Поток закончил работу")
    

worker()
thread = threading.Thread(target=worker)
thread.start()
thread.join()
print("Главный поток завершен")
"""
напоминалка
список напоминаний, в каждом
    сообщение - строка
    задержка в секундах
для каждого напоминания создать Timer, который через указанное время выводит сообщение

сразу запустить все таймеры
дождаться завершения

reminders = [
    ("сообщение 1", 1),
    ("сообщение 2", 2),
    ("сообщение 3", 3),
]
"""
from threading import Timer
import threading
import time
import random

def reminder(message, delay):
    print(f"[{threading.current_thread().name}] Напоминание: {message}")

def main():
    reminders = [
        ("сообщение 1", 1),
        ("сообщение 2", 2),
        ("сообщение 3", 3),
    ]
    
    timers = []

    for message, delay in reminders:
        t = Timer(delay, reminder, args=(message, delay))
        timers.append(t)
        t.start()
        print(f"[{threading.current_thread().name}] Напоминание создано: {message}, срабатывает через {delay} секунд")

    for t in timers:
        t.join()

    print(f"[{threading.current_thread().name}] Все напоминания завершены")

if __name__ == "__main__":
    main()
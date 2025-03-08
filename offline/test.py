class Worker:
    def work(self):
        print("Человек работает")


class RobotWorker:
    def work(self):
        print("Робот работает")


class WorkerService:
    def __init__(self, worker: Worker):
        self.worker = worker

    def manage(self):
        self.worker.work()

#d
from abc import ABC, abstractmethod

class IWorkable(ABC):
    @abstractmethod
    def work(self):
        pass

class Worker(IWorkable):
    def work(self):
        print("Человек работает")

class RobotWorker(IWorkable):
    def work(self):
        print("Робот работает")

class WorkerService:
    def __init__(self, worker: IWorkable):
        self.worker = worker

    def manage(self):
        self.worker.work()
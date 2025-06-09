import logging

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=SingletonMeta):
    def __init__(self, log_file="app.log"):
        self.logger = logging.getLogger("SingletonLogger")

        if not self.logger.hasHandlers():
            self.logger.setLevel(logging.DEBUG)

            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

    def log(self, level, message):
        levels = {
            "info": self.logger.info,
            "warning": self.logger.warning,
            "error": self.logger.error,
            "debug": self.logger.debug
        }
        levels.get(level, self.logger.info)(message)

logger1 = Logger()
logger1.log("info", "запуск")

logger2 = Logger()
logger2.log("error", "ошибка")

print(logger1 is logger2)

import functools


def singleton(cls):
    instances = {}

    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Logger:
    def __init__(self, log_file="app.log"):
        self.logger = logging.getLogger("SingletonLogger")

        if not self.logger.hasHandlers():
            self.logger.setLevel(logging.DEBUG)

            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

    def log(self, level, message):
        levels = {
            "info": self.logger.info,
            "warning": self.logger.warning,
            "error": self.logger.error,
            "debug": self.logger.debug
        }
        levels.get(level, self.logger.info)(message)

logger1 = Logger()
logger1.log("info", "запуск")

logger2 = Logger()
logger2.log("error", "ошибка")

print(logger1 is logger2)
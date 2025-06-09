#logging
"""
отладка
аналитика
мониторинг
документация
"""

#уровни логирования
"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

import logging
logger = logging.getLogger("my_logger")

#обработчики handlers
"""
StreamHandler
FileHandler
SMTPHandler
RotatingFileHandler
TimedRotatingFileHandler
"""

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

#форматтер Formatter

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

#фильтры Filers

class MyFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.ERROR

logger.addFilter(MyFilter())

#конфигурация

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
)
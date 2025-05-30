import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

#сообщения разных уровней
logging.debug("debug")
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
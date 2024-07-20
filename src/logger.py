import logging
import os
from datetime import datetime

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        if not os.path.exists('logs'):
            os.makedirs('logs')
        file_handler = logging.FileHandler(f'logs/{datetime.now().strftime("%Y-%m-%d")}.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger




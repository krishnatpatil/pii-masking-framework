import logging

class Logger:

    def __init__(self):
        logging.basicConfig(filename='logs/app.log', level=logging.INFO)

    def log(self, message):
        logging.info(message)
import sys
import logging
from logging.handlers import RotatingFileHandler

def log(message):
    if message is None:
        print('Abort')
        exit()

    formatter = logging.Formatter('%(asctime)s - %(message)s')
    filename = "logs/location.log"
    logging.basicConfig(filename=filename)
    handler = RotatingFileHandler(
        filename,
        mode='a',
        maxBytes=1024,
        backupCount=2,
        encoding=None,
        delay=0
    )
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    logger = logging.getLogger('LocationLogger')
    logger.propagate = False
    logger.setLevel(logging.INFO)
    logger.handlers = []
    logger.addHandler(handler)

    if isinstance(message, str):
        logger.info(message)

if __name__ == "__main__":
    log(sys.argv[1])
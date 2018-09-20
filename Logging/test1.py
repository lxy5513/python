import logging

DATE_FORMAT = '%m/%d/%Y %H:%M:%S'
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"

logging.basicConfig(level=logging.DEBUG, filename="my.log", format=LOG_FORMAT, datefmt=DATE_FORMAT)


logging.debug("This is a bebug log")
logging.info("This is a info log")
logging.warning("WARNING")
logging.error("ERROR")
logging.critical("CRITICAL")

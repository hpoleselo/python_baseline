import logging

def setup_custom_logger(logger_name: str) -> logging.Logger:
    logging.basicConfig(level=logging.DEBUG,
                format='[%(levelname)s] - [%(funcName)s] - [%(filename)s:%(lineno)d] - [%(asctime)s] - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logger = logging.getLogger(logger_name)
    return logger

def output_logs():
    pass


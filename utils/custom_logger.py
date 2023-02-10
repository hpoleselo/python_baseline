import logging

def setup_custom_logger(logger_name: str, logger_level='DEBUG') -> logging.Logger:
    # TODO: Create dictionary so that when user passes the wished level, it sets up accordingly
    logging.basicConfig(level=logging.DEBUG,
                format='[%(levelname)s] - [%(funcName)s] - [%(filename)s:%(lineno)d] - [%(asctime)s] - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logger = logging.getLogger(logger_name)
    return logger

def output_logs():
    pass


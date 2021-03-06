import logging


def setup_logger(level):
    logger = logging.getLogger()
    logger.setLevel(level)

    s_handler = logging.StreamHandler()
    strg = '[%(levelname)s] %(message)s'
    formatter = logging.Formatter(strg)
    s_handler.setFormatter(formatter)
    logger.addHandler(s_handler)
    s_handler.setLevel(logging.DEBUG)

    f_handler = logging.FileHandler('dencam.log')
    strg = '%(asctime)s | %(levelname)8s | %(name)10s | %(message)s'
    f_formatter = logging.Formatter(strg,
                                    datefmt='%F %H:%M:%S')
    f_handler.setFormatter(f_formatter)
    logger.addHandler(f_handler)
    f_handler.setLevel(logging.DEBUG)

    return logger

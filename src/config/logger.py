import logging
import sys
from config.envs import get_logger_level

_DEFAULT_FORMAT='[%(name)s]: %(message)s'
_LOGGER_NAME='salmorejo'

_logger = None

def get_logger():
    global _logger
    if _logger is None:
        _logger = _get_custom_logger(_LOGGER_NAME, level=get_logger_level())
    return _logger

def _get_custom_logger(logger_name, format=_DEFAULT_FORMAT, level=logging.INFO):
    logger_format = logging.Formatter(format)
    logger_handler = logging.StreamHandler(sys.stdout)
    logger_handler.setFormatter(logger_format)
    logger_handler.setLevel(level)
    logger = logging.getLogger(logger_name)
    logger.addHandler(logger_handler)
    logger.setLevel(level)
    return logger
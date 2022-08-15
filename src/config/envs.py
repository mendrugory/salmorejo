import os
import logging

_LOGGER_LEVEL_NAME="LOGGER_LEVEL"

_DEFAULT_LOGGER_LEVEL=logging._levelToName[logging.INFO]

_logger_level=None

def get_logger_level():
    global _logger_level
    if _logger_level is None:
        _logger_level = logging._nameToLevel[os.getenv(_LOGGER_LEVEL_NAME, _DEFAULT_LOGGER_LEVEL)]
    return _logger_level
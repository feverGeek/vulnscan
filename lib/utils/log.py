import logging
import sys

from lib.core.enums import CUSTOM_LOGGING, EXIT_STATUS

logging.addLevelName(CUSTOM_LOGGING.SYSINFO, '*')
logging.addLevelName(CUSTOM_LOGGING.SUCCESS, '+')
logging.addLevelName(CUSTOM_LOGGING.ERROR, '-')
logging.addLevelName(CUSTOM_LOGGING.WARNING, '!')

LOGGER = logging.getLogger("TookieLogger")

LOGGER_HANDLER = None

try:
    from lib.utils.ansistrm.ansistrm import ColorizingStreamHandler

    try:
        LOGGER_HANDLER = ColorizingStreamHandler(sys.stdout)
        LOGGER_HANDLER.level_map[logging.getLevelName('*')] = (None, 'cyan', False)
        LOGGER_HANDLER.level_map[logging.getLevelName('+')] = (None, 'cyan', False)
        LOGGER_HANDLER.level_map[logging.getLevelName('-')] = (None, 'cyan', False)
        LOGGER_HANDLER.level_map[logging.getLevelName('!')] = (None, 'cyan', False)
    except Exception:
        LOGGER_HANDLER = logging.StreamHandler(sys.stdout)

except ImportError:
    LOGGER_HANDLER = logging.StreamHandler(sys.stdout)

FOMATTER = logging.Formatter('\r[%(levelname)s] %(message)s', '%H:%M:%S')

LOGGER_HANDLER.setFormatter(FOMATTER)
LOGGER.addHandler(LOGGER_HANDLER)
LOGGER.setLevel(CUSTOM_LOGGING.WARNING)


class MY_LOGGER:
    @staticmethod
    def success(msg):
        return LOGGER.log(CUSTOM_LOGGING.SUCCESS, msg)

    @staticmethod
    def info(msg):
        return LOGGER.log(CUSTOM_LOGGING.SYSINFO, msg)

    @staticmethod
    def warning(msg):
        return LOGGER.log(CUSTOM_LOGGING.WARNING, msg)

    @staticmethod
    def error(msg):
        return LOGGER.log(CUSTOM_LOGGING.ERROR, msg)


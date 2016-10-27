import os

from spylogger import get_logger


def __marathon_url():
    url = os.getenv('MARATHON_URL')
    if not url.endswith('/'):
        url += '/'
    return url


def __get_logger():
    return get_logger(
        name=os.getenv('SPY_LOG_LOGGER', 'pretty-no-meta'),
        log_level=os.getenv('SPY_LOG_LEVEL', 'DEBUG')
    )


PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(PACKAGE_DIR)

PLUGIN_FOLDER = os.path.join(PACKAGE_DIR, 'commands')
TEMPLATE_DIR = os.path.join(PACKAGE_DIR, 'templates')

MARATHON_STYLE = os.getenv('MARATHON_STYLE', 'monokai')

MARATHON_URL = __marathon_url()
MARATHON_USER = os.getenv('MARATHON_USER')
MARATHON_PASSWORD = os.getenv('MARATHON_PASSWORD')
MARATHON_AUTH = (MARATHON_USER, MARATHON_PASSWORD)

LOGGER = __get_logger()

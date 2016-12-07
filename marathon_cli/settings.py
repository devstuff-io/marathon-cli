import os

from spylogger import get_logger

from marathon_cli.exceptions import MissingEnvironmentVariable


def __marathon_url():
    version = os.getenv('MARATHON_VERSION', 'v2/')
    if not version.endswith('/'):
        version += '/'

    url = os.getenv('MARATHON_URL')
    try:
        if url.endswith(version):
            url = url.replace(version, '')
        if not url.endswith('/'):
            url += '/'
    except AttributeError:
        raise MissingEnvironmentVariable('MARATHON_URL')
    return (url, version)


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

MARATHON_URL, MARATHON_VERSION = __marathon_url()
MARATHON_USER = os.getenv('MARATHON_USER')
MARATHON_PASSWORD = os.getenv('MARATHON_PASSWORD')
MARATHON_AUTH = (MARATHON_USER, MARATHON_PASSWORD)

LOGGER = __get_logger()

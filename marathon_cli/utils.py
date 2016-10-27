import os

from spylogger import get_logger

from marathon_cli.settings import TEMPLATE_DIR

LOGGER = get_logger(name='pretty-no-meta', log_level='DEBUG')


def read_template(filename):
    return open(os.path.join(TEMPLATE_DIR, filename)).read()

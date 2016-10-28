import os
import pickle

from marathon_cli.settings import TEMPLATE_DIR


def read_template(filename):
    return open(os.path.join(TEMPLATE_DIR, filename)).read()


def pickle_object(obj, filename):
    pickle.dump(obj, open(filename, 'w'))

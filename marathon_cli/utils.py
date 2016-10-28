import os
import pickle
from uuid import uuid4

from marathon_cli.settings import TEMPLATE_DIR


def read_template(filename):
    return open(os.path.join(TEMPLATE_DIR, filename)).read()


def get_pickle_ext():
    return '-%s.pickle' % str(uuid4())


def pickle_object(obj, filename):
    filename += get_pickle_ext()
    pickle.dump(obj, open(filename, 'w'))

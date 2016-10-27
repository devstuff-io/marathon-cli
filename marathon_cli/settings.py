import os

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(PACKAGE_DIR)

PLUGIN_FOLDER = os.path.join(PACKAGE_DIR, 'commands')
TEMPLATE_DIR = os.path.join(PACKAGE_DIR, 'templates')

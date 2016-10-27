from unittest import TestCase

from click.testing import CliRunner

from marathon_cli import main as marathon
from tests import COMMAND_OPTS


class MarathonMainCliTest(TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def tearDown(self):
        pass

    def test_cmd_help(self):
        result = self.runner.invoke(marathon, ['--help'])
        for opt in COMMAND_OPTS:
            self.assertIn(opt, result.output)

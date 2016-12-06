from unittest import TestCase

from click.testing import CliRunner

from marathon_cli import main as marathon, __version__ as version
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

    def test_cmd_version(self):
        result = self.runner.invoke(marathon, ['--version'])
        self.assertEqual(
            'marathon version {}\n'.format(version),
            result.output
        )

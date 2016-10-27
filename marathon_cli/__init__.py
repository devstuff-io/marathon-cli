import os

import click

from marathon_cli.settings import PLUGIN_FOLDER


class MarathonCli(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(PLUGIN_FOLDER):
            if filename == '__init__.py':
                continue
            if filename.endswith('.py'):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(PLUGIN_FOLDER, name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']


main = MarathonCli(
    help='cli helpers for the marathon api.',
    context_settings=dict(
        help_option_names=['-h', '--help', '?']
    )
)


if __name__ == '__main__':
    main()

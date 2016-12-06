import os

import click

from marathon_cli.settings import PLUGIN_FOLDER, LOGGER

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('marathon version {}'.format(__version__))
    ctx.exit()


def get_command(name):
    ns = {}
    fn = os.path.join(PLUGIN_FOLDER, name + '.py')
    try:
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
            return ns['cli']
    except IOError:
        LOGGER.error('command does not exist: {}'.format(name))


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
        return get_command(name)


@click.group(context_settings=CONTEXT_SETTINGS, cls=MarathonCli)
@click.option('--version', is_flag=True, callback=print_version, expose_value=False,
              is_eager=True, help='print the installed version and exit')
@click.pass_context
def main(ctx):
    """cli helpers for the marathon api."""
    ctx.obj = {}
    ctx.obj['logger'] = LOGGER


if __name__ == '__main__':
    main()


__version__ = '1.1.7'

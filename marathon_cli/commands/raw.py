import click
from pretty_json import format_json

from marathon_cli.settings import LOGGER
from marathon_cli.utils import pickle_object
from marathon_cli.x import get

_savefile_tmpl = 'raw-{}'


@click.command()
@click.option('-p', '--pickle', 'pickle_it', is_flag=True, help='pickle the response object and save it')
@click.option('-m', '--method', default='GET')
@click.argument('uri')
@click.argument('options', nargs=-1)
def cli(uri, options, method, pickle_it):
    """Call the given uri.

    Example:

    ::

        marathon raw --pickle groups
    """
    method = method.upper()
    LOGGER.debug({'uri': uri, 'options': options, 'method': method})

    response = get(uri)

    if pickle_it:
        pickle_object(response, _savefile_tmpl.format(uri.replace('/', '__')))

    click.echo(format_json(response.json()))


if __name__ == '__main__':
    cli()

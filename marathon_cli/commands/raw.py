import click

from marathon_cli.output import format_json
from marathon_cli.settings import LOGGER
from marathon_cli.x import get


@click.command()
@click.option('-m', '--method', default='GET')
@click.argument('uri')
@click.argument('options', nargs=-1)
def cli(uri, options, method):
    """Call the given uri.
    """
    method = method.upper()
    LOGGER.debug({'uri': uri, 'options': options, 'method': method})

    response = get(uri).json()
    click.echo(format_json(response))


if __name__ == '__main__':
    cli()

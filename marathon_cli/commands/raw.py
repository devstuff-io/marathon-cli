import click
from pretty_json import format_json

from marathon_cli.utils import pickle_object
from marathon_cli.x import get_method


@click.command()
@click.option('--dry-run', is_flag=True, help='generate the request and show it - do not send to marathon')
@click.option('-p', '--pickle', 'pickle_it', is_flag=True, help='pickle the response object and save it')
@click.option('-m', '--method', default='GET')
@click.argument('uri')
@click.argument('options', nargs=-1)
@click.pass_context
def cli(ctx, uri, options, method, pickle_it, dry_run):
    """Call the given uri.

    Example:

    ::

        marathon raw --pickle groups
    """
    ctx.obj['logger'].debug({'uri': uri, 'options': options, 'method': method})

    method = get_method(method)
    response = method(uri)

    if pickle_it:
        pickle_object(response, 'raw-{}'.format(uri.replace('/', '__')))

    click.echo(format_json(response.json()))

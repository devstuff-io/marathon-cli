import click
from pretty_json import format_json

from marathon_cli.utils import pickle_object
from marathon_cli.x import get


@click.command()
@click.option('-p', '--pickle', 'pickle_it', is_flag=True, help='pickle the response object and save it')
@click.pass_context
def cli(ctx, pickle_it, *args, **kwargs):
    """Get info about the Marathon Instance.

    .. versionadded:: 1.1.7

    """
    response = get('info')
    ctx.obj['logger'].debug({'response': response})

    if pickle_it:
        pickle_object(response, 'info')

    click.echo(format_json(response.json()))

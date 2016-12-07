import click

from marathon_cli.commands import get_request


@click.command()
@click.option('-p', '--pickle', 'pickle_it', is_flag=True, help='pickle the response object and save it')
@click.pass_context
def cli(ctx, pickle_it, *args, **kwargs):
    """Returns the current leader.

    .. versionadded:: 1.1.8

    """
    click.echo(get_request(ctx, 'leader', pickle_it))

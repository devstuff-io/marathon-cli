import click
from pretty_json import format_json

from marathon_cli.utils import pickle_object
from marathon_cli.x import get

_savefile_tmpl = 'tasks'


@click.command()
@click.option('-p', '--pickle', 'pickle_it', is_flag=True, help='pickle the response object and save it')
def cli(pickle_it):
    """Get all running tasks.
    """
    tasks = get('tasks')

    if pickle_it:
        pickle_object(tasks, _savefile_tmpl)

    click.echo(format_json(tasks.json()))


if __name__ == '__main__':
    cli()

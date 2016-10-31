import click
from pretty_json import format_json

from marathon_cli.settings import LOGGER
from marathon_cli.utils import pickle_object
from marathon_cli.x import get

_savefile_tmpl = 'app-tasks-{}'


@click.command()
@click.option('-p', '--pickle', 'pickle_it', is_flag=True, help='pickle the response object and save it')
@click.argument('app_id')
def cli(app_id, pickle_it):
    """Get app tasks.
    """
    uri = 'apps/%s/tasks/' % app_id
    LOGGER.debug({'app_id': app_id, 'uri': uri})

    tasks = get(uri)

    if pickle_it:
        pickle_object(tasks, _savefile_tmpl.format(app_id))

    tasks = tasks.json()
    tasks = tasks.get('tasks')
    click.echo(format_json({'app_tasks': tasks, 'count': len(tasks)}))


if __name__ == '__main__':
    cli()

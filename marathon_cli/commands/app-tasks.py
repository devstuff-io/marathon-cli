import click
from pretty_json import format_json

from marathon_cli.utils import pickle_object
from marathon_cli.x import get


@click.command()
@click.option('-p', '--pickle', 'pickle_it', is_flag=True, help='pickle the response object and save it')
@click.argument('app_id')
@click.pass_context
def cli(ctx, app_id, pickle_it):
    """Get app tasks.
    """
    uri = 'apps/%s/tasks/' % app_id
    ctx.obj['logger'].debug({'app_id': app_id, 'uri': uri})

    tasks = get(uri)

    if pickle_it:
        pickle_object(tasks, 'app-tasks-{}'.format(app_id))

    tasks = tasks.json()
    tasks = tasks.get('tasks')
    click.echo(format_json({'app_tasks': tasks, 'count': len(tasks)}))

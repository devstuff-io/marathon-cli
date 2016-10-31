import click
from pretty_json import format_json

from marathon_cli.settings import LOGGER
from marathon_cli.utils import pickle_object
from marathon_cli.x import delete

_savefile_tmpl = 'delete-app-tasks-{}'


def __pickle_it(thing, uri):
    pickle_object(
        thing,
        _savefile_tmpl.format(uri.replace('/', '__'))
    )


@click.command()
@click.option('-p', '--pickle', 'pickle_it', is_flag=True, help='pickle the response object and save it')
@click.argument('app_id')
@click.argument('app_tasks', nargs=-1)
def cli(app_id, app_tasks, pickle_it):
    """Kill app tasks.

    Kill all tasks when no task is given.
    If a task id is provided, kill only that task.
    If multiple tasks are provided, kill those tasks.
    """
    uri = 'apps/%s/tasks/' % app_id
    LOGGER.debug({'app_id': app_id, 'tasks': app_tasks, 'uri': uri})

    responses = []

    if len(app_tasks) == 1:
        uri += app_tasks[0]

    if len(app_tasks) > 1:
        for task_id in app_tasks:
            if not task_id.startswith('/'):
                task_id = '/' + task_id
            LOGGER.info({'DELETE': uri + task_id})
            thing = delete(uri + task_id)
            if pickle_it:
                __pickle_it(thing, uri + task_id)
            responses.append(thing.json())
    else:
        LOGGER.info({'DELETE': uri})
        thing = delete(uri)
        if pickle_it:
            __pickle_it(thing, uri)
        responses.append(thing.json())

    click.echo(format_json({'Killed': responses}))


if __name__ == '__main__':
    cli()

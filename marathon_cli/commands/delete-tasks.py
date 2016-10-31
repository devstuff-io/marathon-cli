import click
from pretty_json import format_json

from marathon_cli.settings import LOGGER
from marathon_cli.utils import pickle_object
from marathon_cli.x import post

_savefile_tmpl = 'delete-tasks'


@click.command()
@click.option('-p', '--pickle', 'pickle_it', is_flag=True, help='pickle the response object and save it')
@click.option('-s', '--scale', 'scale', is_flag=True, help='Scale the app down')
@click.option('-w', '--wipe', 'wipe', is_flag=True, help='Associated dynamic reservations will be unreserved, and persistent volumes will be destroyed.')
@click.argument('task_ids', nargs=-1)
def cli(wipe, scale, pickle_it, task_ids):
    """Delete specified task ids.
    """
    LOGGER.debug({'wipe': wipe, 'scale': scale, 'pickle_it': pickle_it, 'task_ids': task_ids})

    delete_task_ids = []
    for tid in task_ids:
        delete_task_ids.append(tid)
    LOGGER.debug({'delete_task_ids': delete_task_ids})

    tasks = post('tasks/delete', json={"ids": delete_task_ids})

    if pickle_it:
        pickle_object(tasks, _savefile_tmpl)

    click.echo(format_json(tasks.json()))


if __name__ == '__main__':
    cli()

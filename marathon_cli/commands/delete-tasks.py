import click
from pretty_json import format_json

from marathon_cli.utils import pickle_object
from marathon_cli.x import post


@click.command()
@click.option('--dry-run', is_flag=True, help='generate the request and show it - do not send to marathon')
@click.option('-p', '--pickle', 'pickle_it', is_flag=True, help='pickle the response object and save it')
@click.option('-s', '--scale', 'scale', is_flag=True, help='Scale the app down')
@click.option('-w', '--wipe', 'wipe', is_flag=True, help='Associated dynamic reservations will be unreserved, and persistent volumes will be destroyed.')
@click.argument('task_ids', nargs=-1)
@click.pass_context
def cli(ctx, wipe, scale, pickle_it, task_ids, dry_run):
    """Delete specified task ids.
    """
    uri = 'tasks/delete'
    ctx.obj['logger'].debug({'uri': uri, 'wipe': wipe, 'scale': scale, 'pickle_it': pickle_it, 'task_ids': task_ids, 'dry_run': dry_run})

    delete_task_ids = []
    for tid in task_ids:
        delete_task_ids.append(tid)
    ctx.obj['logger'].debug({'delete_task_ids': delete_task_ids})

    if dry_run:
        click.echo(format_json({'[DryRun] POST': uri}))
        return

    tasks = post(uri, json={"ids": delete_task_ids})

    if pickle_it:
        pickle_object(tasks, 'delete-tasks')

    click.echo(format_json(tasks.json()))

import click
from pretty_json import format_json

from marathon_cli.utils import pickle_object
from marathon_cli.x import delete


def __pickle_it(thing, uri):
    pickle_object(
        thing,
        'delete-app-tasks-{}'.format(uri.replace('/', '__'))
    )


@click.command()
@click.option('--dry-run', is_flag=True, help='generate the request and show it - do not send to marathon')
@click.option('-p', '--pickle', 'pickle_it', is_flag=True, help='pickle the response object and save it')
@click.argument('app_id')
@click.argument('app_tasks', nargs=-1)
@click.pass_context
def cli(ctx, app_id, app_tasks, pickle_it, dry_run):
    """Kill app tasks.

    Kill all tasks when no task is given.
    If a task id is provided, kill only that task.
    If multiple tasks are provided, kill those tasks.
    """
    uri = 'apps/%s/tasks/' % app_id
    ctx.obj['logger'].debug({'app_id': app_id, 'tasks': app_tasks, 'uri': uri})

    responses = []

    if len(app_tasks) == 1:
        uri += app_tasks[0]

    if len(app_tasks) > 1:
        for task_id in app_tasks:
            if not task_id.startswith('/'):
                task_id = '/' + task_id
            if dry_run:
                click.echo(format_json({'[DryRun] DELETE': uri + task_id}))
            else:
                ctx.obj['logger'].info({'DELETE': uri + task_id})
                thing = delete(uri + task_id)
                if pickle_it:
                    __pickle_it(thing, uri + task_id)
                responses.append(thing.json())
    else:
        if dry_run:
            click.echo(format_json({'[DryRun] DELETE': uri}))
        else:
            ctx.obj['logger'].info({'DELETE': uri})
            thing = delete(uri)
            if pickle_it:
                __pickle_it(thing, uri)
            responses.append(thing.json())

    click.echo(format_json({'Killed': responses}))

import click
from pretty_json import format_json

from marathon_cli.utils import pickle_object
from marathon_cli.x import post


@click.command()
@click.option('--dry-run', is_flag=True, help='generate the request and show it - do not send to marathon')
@click.option('--force', is_flag=True, help='force the app to restart')
@click.option('-p', '--pickle', 'pickle_it', is_flag=True, help='pickle the response object and save it')
@click.argument('app_id')
@click.pass_context
def cli(ctx, app_id, pickle_it, dry_run, force):
    """Restart app.

    :param app_id: **required**. Ensure create or update app with this name
    :type app_id: str

    Example:

    ::

        marathon restart-app --pickle my-app
    """
    uri = 'apps/%s/restart' % app_id
    ctx.obj['logger'].debug({'app_id': app_id, 'uri': uri})

    if force:
        uri += '?force=true'

    if dry_run:
        click.echo(format_json({'[DryRun] POST': uri}))
        return

    response = post(uri)
    ctx.obj['logger'].debug({'response': response})

    if pickle_it:
        pickle_object(response, 'restart-app-{}'.format(app_id))

    click.echo(format_json(response.json()))

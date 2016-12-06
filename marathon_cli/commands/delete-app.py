import click
from pretty_json import format_json

from marathon_cli.utils import pickle_object
from marathon_cli.x import delete


@click.command()
@click.option('--dry-run', is_flag=True, help='generate the request and show it - do not send to marathon')
@click.option('-p', '--pickle', 'pickle_it', is_flag=True, help='pickle the response object and save it')
@click.argument('app_id')
@click.pass_context
def cli(ctx, app_id, pickle_it, dry_run):
    """Destroy app.

    :param app_id: **required**. Ensure create or update app with this name
    :type app_id: str

    Example:

    ::

        marathon delete-app --pickle my-app
    """
    uri = 'apps/%s' % app_id
    ctx.obj['logger'].debug({'app_id': app_id, 'uri': uri})

    if dry_run:
        click.echo(format_json({'[DryRun] DELETE': uri}))
        return

    response = delete(uri)
    ctx.obj['logger'].debug({'response': response})

    if pickle_it:
        pickle_object(response, 'delete-app-{}'.format(app_id))

    click.echo(format_json(response.json()))

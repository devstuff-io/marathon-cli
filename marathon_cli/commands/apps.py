import click
from pretty_json import format_json

from marathon_cli.utils import pickle_object
from marathon_cli.x import get


@click.command()
@click.option('-p', '--pickle', 'pickle_it', is_flag=True, help='pickle the response object and save it')
@click.argument('app_ids', nargs=-1)
@click.pass_context
def cli(ctx, app_ids, pickle_it):
    """Get apps deployed to a marathon instance.

    Retrieve all apps when no app ids are given.
    If an app id is provided, send a GET request for only that app id.
    If multiple app ids are provided, find those apps and return them.
    """
    ctx.obj['logger'].info('Get all apps deployed to a marathon instance.')

    uri = 'apps/'
    if len(app_ids) == 1:
        uri += app_ids[0]

    ctx.obj['logger'].debug({'app_ids': app_ids, 'uri': uri})

    apps = get(uri)

    if pickle_it:
        pickle_object(apps, 'apps')

    apps = apps.json()

    if len(app_ids) == 1:
        click.echo(format_json(apps))
        return

    response = {'apps': [], 'count': 0}
    apps = apps.get('apps')

    if len(app_ids) > 1:
        for app_id in app_ids:
            if not app_id.startswith('/'):
                app_id = '/' + app_id
            for app in apps:
                if app.get('id') == app_id:
                    response['apps'].append(app)
    else:
        response['apps'] = apps

    response['count'] = len(response['apps'])
    click.echo(format_json(response))

import click

from marathon_cli.output import format_json
from marathon_cli.settings import LOGGER
from marathon_cli.x import get


@click.command()
@click.argument('app_ids', nargs=-1)
def cli(app_ids):
    """Get apps deployed to a marathon instance.

    Retrieve all apps when no app ids are given.
    If an app id is provided, send a GET request for only that app id.
    If multiple app ids are provided, find those apps and return them.
    """
    LOGGER.info('Get all apps deployed to a marathon instance.')

    uri = 'apps/'
    if len(app_ids) == 1:
        uri += app_ids[0]

    LOGGER.debug({'app_ids': app_ids, 'uri': uri})

    apps = get(uri).json()

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


if __name__ == '__main__':
    cli()

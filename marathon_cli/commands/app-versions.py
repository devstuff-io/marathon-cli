import click

from marathon_cli.output import format_json
from marathon_cli.settings import LOGGER
from marathon_cli.x import get


@click.command()
@click.argument('app_id')
@click.argument('app_versions', nargs=-1)
def cli(app_id, app_versions):
    """Get app versions.

    Retrieve all versions when no version is given.
    If a version id is provided, send a GET request for only that app version.
    If multiple versions are provided, find those app versions and return them.
    """
    uri = 'apps/%s/versions/' % app_id
    if len(app_versions) == 1:
        uri += app_versions[0]

    LOGGER.debug({'app_id': app_id, 'versions': app_versions, 'uri': uri})
    versions = get(uri).json()

    if len(app_versions) == 1:
        click.echo(format_json(versions))
        return

    response = {'app_versions': [], 'count': 0}
    versions = versions.get('versions')

    if len(app_versions) > 1:
        for version_id in app_versions:
            if not version_id.startswith('/'):
                version_id = '/' + version_id
            for version in versions:
                if version == version_id:
                    response['app_versions'].append(get(uri + version_id))
    else:
        response['app_versions'] = versions

    response['count'] = len(response['app_versions'])
    click.echo(format_json(response))


if __name__ == '__main__':
    cli()

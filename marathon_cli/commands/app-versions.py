import click
from pretty_json import format_json

from marathon_cli.settings import LOGGER
from marathon_cli.utils import pickle_object
from marathon_cli.x import get

_savefile_tmpl = 'app-versions-{}'


@click.command()
@click.option('-p', '--pickle', 'pickle_it', is_flag=True, help='pickle the response object and save it')
@click.argument('app_id')
@click.argument('app_versions', nargs=-1)
def cli(app_id, app_versions, pickle_it):
    """Get app versions.

    Retrieve all versions when no version is given.
    If a version id is provided, send a GET request for only that app version.
    If multiple versions are provided, find those app versions and return them.
    """
    uri = 'apps/%s/versions/' % app_id
    if len(app_versions) == 1:
        uri += app_versions[0]

    LOGGER.debug({'app_id': app_id, 'versions': app_versions, 'uri': uri})
    versions = get(uri)

    if pickle_it:
        pickle_object(versions, _savefile_tmpl.format(app_id))

    versions = versions.json()

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

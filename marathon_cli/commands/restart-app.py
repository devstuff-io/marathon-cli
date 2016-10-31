import click
from pretty_json import format_json

from marathon_cli.settings import LOGGER
from marathon_cli.utils import pickle_object
from marathon_cli.x import post

_savefile_tmpl = 'restart-app-{}'


@click.command()
@click.option('-p', '--pickle', 'pickle_it', is_flag=True, help='pickle the response object and save it')
@click.argument('app_id')
def cli(app_id, pickle_it):
    """Restart app.

    :param app_id: **required**. Ensure create or update app with this name
    :type app_id: str

    Example:

    ::

        marathon restart-app --pickle my-app
    """
    uri = 'apps/%s/restart' % app_id
    LOGGER.debug({'app_id': app_id, 'uri': uri})

    response = post(uri)
    LOGGER.debug({'response': response})

    if pickle_it:
        pickle_object(response, _savefile_tmpl.format(app_id))

    click.echo(format_json(response.json()))


if __name__ == '__main__':
    cli()

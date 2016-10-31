import click
from pretty_json import format_json

from marathon_cli.settings import LOGGER
from marathon_cli.utils import pickle_object
from marathon_cli.x import delete

_savefile_tmpl = 'delete-app-{}'


@click.command()
@click.option('-p', '--pickle', 'pickle_it', is_flag=True, help='pickle the response object and save it')
@click.argument('app_id')
def cli(app_id, pickle_it):
    """Destroy app.

    :param app_id: **required**. Ensure create or update app with this name
    :type app_id: str

    Example:

    ::

        marathon delete-app --pickle my-app
    """
    uri = 'apps/%s' % app_id
    LOGGER.debug({'app_id': app_id, 'uri': uri})

    response = delete(uri)
    LOGGER.debug({'response': response})

    if pickle_it:
        pickle_object(response, _savefile_tmpl.format(app_id))

    click.echo(format_json(response.json()))


if __name__ == '__main__':
    cli()

import json
import os

import click
from jinja2 import Template
from pretty_json import format_json

from marathon_cli.settings import LOGGER
from marathon_cli.utils import pickle_object
from marathon_cli.x import put

_savefile_tmpl = 'put-app-{}'


@click.command()
@click.option('-p', '--pickle', 'pickle_it', is_flag=True, help='pickle the response object and save it')
@click.option('--dry-run', is_flag=True, help='generate the request and show it - do not send to marathon')
@click.argument('app_id')
@click.argument('template_file', type=click.File('rb'))
@click.argument('template_vars', nargs=-1)
def cli(app_id, template_file, template_vars, pickle_it, dry_run):
    """Update or create an app with id.

    :param app_id: **required**. Ensure create or update app with this name
    :type app_id: str

    :param template_file: **required**. jinja template file
    :type template_file: file

    :param template_vars: key value pairs used by the jinja template.

        - Environment variables: ``env=VAR_NAME``
        - Contents of a file: ``file=FILE_NAME``

    :type template_vars: mapping

    Example:

    ::

        marathon put-app --dry-run --pickle my-app app.json.j2 prj_key=foo env=AWS_ACCOUNT_ID app_env=dev file=VERSION
    """
    uri = 'apps/' + app_id
    LOGGER.debug({'app_id': app_id, 'uri': uri, 'template_file': template_file, 'template_vars': template_vars})

    jinja_vars = {'app_id': app_id}
    if template_vars:
        for var in template_vars:
            (key, value) = var.split('=')
            if key == 'env':
                key = value
                value = os.getenv(value)
            elif key == 'file':
                key = value
                value = open(key).read().strip()

            jinja_vars[key] = value

    app_request = Template(template_file.read()).render(**jinja_vars)
    app_request = json.loads(app_request)

    if dry_run:
        click.echo(format_json(app_request))
        return

    response = put(uri, json=app_request)
    LOGGER.debug({'response': response})

    if pickle_it:
        pickle_object(response, _savefile_tmpl.format(app_id))

    click.echo(format_json(response.json()))


if __name__ == '__main__':
    cli()

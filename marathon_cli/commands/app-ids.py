import click
import jmespath
from pretty_json import format_json

from marathon_cli.x import get


@click.command()
@click.pass_context
def cli(ctx):
    """Get the ids of all apps deployed to a marathon instance.
    """
    ctx.obj['logger'].debug('Get the ids of all apps deployed to a marathon instance.')
    apps = get('apps').json()
    apps = sorted(jmespath.search('apps[*].id', apps))
    click.echo(format_json({'app-ids': apps, 'count': len(apps)}))

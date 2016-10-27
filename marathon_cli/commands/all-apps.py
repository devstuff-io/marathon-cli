import click

from marathon_cli.utils import LOGGER


@click.command()
def cli():
    """Get all containers deployed to a marathon instance.
    """
    LOGGER.debug('Get all containers deployed to a marathon instance.')
    click.echo('Get all containers deployed to a marathon instance.')
    LOGGER.info('DONE')


if __name__ == '__main__':
    cli()

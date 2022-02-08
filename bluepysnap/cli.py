"""The project's command line launcher."""
import click

from bluepysnap.circuit_validation import validate


@click.group()
def cli():
    """The CLI object."""


@cli.command('validate', short_help='Validate Sonata circuit')
@click.argument('config_file', type=click.Path(exists=True, file_okay=True, dir_okay=False))
@click.option('--bbp-check', is_flag=True, help='validate the config using BBP specification')
def validate_cli(config_file, bbp_check):
    """Cli command for validating of Sonata circuit.

    Args:
        config_file: path to Sonata circuit config file
    """
    validate(config_file, bbp_check=bbp_check)

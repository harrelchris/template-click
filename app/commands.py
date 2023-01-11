import click

from app.submodule.commands import run


@click.group()
def cli():
    pass


cli.add_command(run)

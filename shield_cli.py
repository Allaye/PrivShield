import os
import click
from shield.shield import Shield
from shield.util import prep_files, clean_files


class ShieldCli:
    """
    class that contains methods for scanning, adding and exempting files
    TODO: bring in some of the functions into the class and class through a click group
    """

    def __init__(self):
        self.cwd = os.getcwd()
        self.fileignore_path = os.path.abspath(".shield.lock/.fileignore")
        self.keyignore_path = os.path.abspath(".shield.lock/.keyignore")
        self.file_content = Shield().load_paths(self.fileignore_path, self.keyignore_path)


@click.group(invoke_without_command=True)
@click.pass_context
@click.option('-l', '--list', is_flag=True, help='List all the guarded words')
@click.option('-inc', '--include', nargs=1,
              help='include a file to be scanned by removing it\'s name from  .shield.lock/.fileignore')
def cli(ctx, list, include):
    if ctx.invoked_subcommand is None:
        if list:
            fileignore_path = os.path.abspath(".shield.lock/.fileignore")
            keyignore_path = os.path.abspath(".shield.lock/.keyignore")
            file_content = Shield().load_paths(fileignore_path, keyignore_path)
            click.echo(file_content["guarded_words"])
        if include:
            exempted_files = [str(file.strip())
                              for file in open('.shield.lock/.fileignore').readlines()]
            try:
                with open('.shield.lock/.fileignore', 'r') as f:
                    lines = f.readlines()
                    f.close()
                with open('.shield.lock/.fileignore', 'w') as f:
                    for line in lines:
                        if line.strip("\n") != include:
                            f.write(line)
                        else:
                            exempted_files.remove(line.strip("\n"))
                            click.secho(
                                f"Removed `{include}` from .fileignore", fg='green')
                    f.close()
            except FileNotFoundError:
                click.secho("Please initialize the PrivShield first", fg='red')
        elif not list and not include:
            click.secho(
                "Env Scanning tool PrivShield. To get help use the `--help` flag for the list of options and "
                "commands available",
                fg='green')


@cli.command()
def init():
    """create .shield.lock folder and create .fileignore and .keyignore files"""
    click.secho("PrivShield been Initialed...", fg='green')
    prep_files()


@cli.command()
def clean():
    """Removing all directories and files created."""
    click.secho("Removing all directories and files created....", fg='yellow')
    clean_files()


@cli.command()
@click.argument('path', type=click.Path(dir_okay=True), default=os.getcwd(), required=False)
def skim(path):
    """Scan the project for any key or token"""
    fileignore_path = os.path.abspath(".shield.lock/.fileignore")
    keyignore_path = os.path.abspath(".shield.lock/.keyignore")
    '''Scan the project for any key or token'''
    try:
        Shield().search(path, fileignore_path, keyignore_path)
        click.echo(click.style("\nScanning completed successfully", fg='green'))
    except FileNotFoundError:
        click.echo(click.style("\nCould not complete scan, make sure key-guard is initialized\n", fg='red'))


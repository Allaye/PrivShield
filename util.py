import os
import click


def prep_files():
    """
    write .fileignore and .keyignore files to the project root
    """
    try:
        click.secho("Creating default lookup directory", fg='green')
        os.mkdir('.guard')
        click.secho("Changing current directory to default directory", fg='green')
        os.chdir('.guard')
        click.secho("Creating default lookup directories", fg='green')
        with open('.fileignore', 'w') as f:
            f.writelines(['.git\n', '.guard\n', '.vscode\n', '.idea\n', '.pytest_cache\n',
                          '__pycache__\n', 'venv\n', 'node_modules\n', '.env\n', '.venv\n'])
            f.close()
        click.secho(".fileignore file created and populated", fg='green')
        with open('.keyignore', 'w') as f:
            f.writelines(['key =\n', 'access_key =\n', 'auth_key =\n',
                          'password =\n', 'secret =\n', 'token =\n', 'access_token =\n'])
            f.close()
        click.secho(".keyignore file created and populated", fg='green')
    except FileExistsError:
        click.secho("key_guard is already initialized", fg='yellow')
        pass
    except InterruptedError:
        click.secho("privshield initialization was interrupted", fg='yellow')
        pass
    except PermissionError:
        click.secho("Error you dont have permission for i/o operation", fg='red')
        pass
    # general exception
    except Exception as e:
        click.secho(f"Error: {e}", fg='red')
        pass


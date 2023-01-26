import os
import click


def prep_files():
    """
    write .fileignore and .keyignore files to the project root
    """
    try:
        click.secho("Creating default lookup directory", fg='green')
        os.mkdir('.shield.lock')
        click.secho("Changing current directory to default directory", fg='green')
        os.chdir('.shield.lock')
        click.secho("Creating default lookup directories", fg='green')
        with open('.fileignore', 'w') as f:
            f.writelines(['.git\n', '.shield.lock\n', '.vscode\n', '.idea\n', '.pytest_cache\n',
                          '__pycache__\n', 'venv\n', 'node_modules\n', '.env\n', '.venv\n'])
            f.close()
        click.secho(".fileignore file created and populated", fg='green')
        with open('.keyignore', 'w') as f:
            f.writelines(['key =\n', 'access_key =\n', 'auth_key =\n',
                          'password =\n', 'secret =\n', 'token =\n', 'access_token =\n'])
            f.close()
        click.secho(".keyignore file created and populated", fg='green')
    except FileExistsError:
        click.secho("PrivShield is already initialized", fg='yellow')
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


def clean_files(ignore_path='/.shield.lock'):
    """
    remove .fileignore and .keyignore files from the project root
    """
    try:
        if os.getcwd() == '.shield.lock':
            click.secho("Removing default lookup directory and files", fg='green')
            os.remove('.keyignore')
            os.remove('.fileignore')
            os.chdir('..')
            os.rmdir('.shield.lock')
            click.secho("lookup files and directory has been removed", fg='green')
        else:
            os.chdir(ignore_path)
            click.secho("Removing default lookup directory and files", fg='green')
            os.remove('.keyignore')
            os.remove('.fileignore')
            os.chdir('..')
            os.rmdir('.shield.lock')
            click.secho("lookup files and directory has been removed", fg='green')
    except FileNotFoundError:
        click.secho("cant find lookup folder or privshield is not initialized", fg='yellow')
        pass
    except InterruptedError:
        click.secho("privshield initialization was interrupted", fg='yellow')
        pass
    except PermissionError:
        click.secho("Error you dont have permission for i/o operation", fg='red')
        pass
    except Exception as e:
        click.secho(f"Error: {e}", fg='red')
        pass


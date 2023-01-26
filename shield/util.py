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
    
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


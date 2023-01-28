# Description: Shield class for privshield
# author: Kolade Gideon @Allaye
# created: 2022-06-10
# last modified: 2023-01-28

import os
import click


class Shield:
    """
    class that contains methods for scanning, adding and exempting files

    methods:
    load_paths: load contents of .fileignore and .keyignore and return them in a dict object
    search: search text method used in scanning
    TODO: add methods for adding and exempting files
    """
    @staticmethod
    def load_paths(fileignore_path, keyignore_path):
        """
        load contents of .fileignore and .keyignore and return them in a dict object
        Transpose of the array.

        Returns
        -------
        ret
            A dict object containing the contents of .fileignore and .keyignore
        """
        try:
            guarded_words = [str(word.strip())
                             for word in open(keyignore_path).readlines()]
            exempted_files = [str(file.strip())
                              for file in open(fileignore_path).readlines()]
            return {"guarded_words": guarded_words, "exempted_files": exempted_files}
        except FileNotFoundError:
            click.echo(click.style("\nmake sure key-guard is initialized\n", fg='red'))

    
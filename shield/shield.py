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

    def search(self, path, fileignore_path, keyignore_path):
        """
        search text method used in scanning

        """
        file_contents = self.load_paths(fileignore_path,
                                        keyignore_path)
        os.chdir('..')
        os.chdir(path)
        path = os.listdir(path)
        for fname in path[::-1]:
            abs_path = os.path.abspath(fname)
            if os.path.isfile(abs_path):
                try:
                    if os.path.basename(fname) not in file_contents["exempted_files"] and not os.path.basename(
                            fname).startswith('.'):
                        for l_no, line in enumerate(open(fname, 'r')):
                            for word in file_contents["guarded_words"]:
                                if word in line:
                                    click.echo(click.style(
                                        f"Warning: '{word}' found in `{fname.split('/')[-1]}` Kindly check for line: `{l_no}` -> '{line.strip()}' to make sure you don't commit sensitive data.",
                                        fg='yellow'))

                        path.remove(os.path.basename(fname))
                except UnicodeDecodeError:
                    pass
            elif os.path.isdir(abs_path) and not os.path.basename(abs_path).startswith('.'):
                print(f"Scanning {abs_path}")
                self.search(abs_path, fileignore_path, keyignore_path)
                path.remove(os.path.basename(abs_path))
                os.chdir('..')

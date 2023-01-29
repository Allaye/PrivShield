# privshield 

A lightweight cli tool to scan projects for exposed credentials and keys.

## Key Features

- [x] Skim/Scan Project for exposed credentials
- [x] add folders and file to be ignored from the tool
- [x] include files to be processed by the tool
- [x] update files and look out for new keywords


## Setting up the tool for local development
### Note: This tool is only tested on windows os
- Clone this repository to your local machine.
- Create a virtual environment for your project and activate it. Install all dependencies from  requirements.txt file.

```bash
python -m venv shieldvenv/
pip install -r requirements.txt
```


- Quick start up tool by running:

```bash
shield_cli skim
```

- Add the `--help` option the command to check out the available options.

```bash
Usage: shield_cli [OPTIONS] COMMAND [ARGS]...

Options:
  --help                Show this message and exit.

Commands:
  add - Add key to be ignored
  clean - Clean all files generated by the tool
  ignore - ignore  a file from been scanned
  init - Initialize the tool for use, it will create some directories and... 
  skim - Skim through the project for any key or token
```




## Contributing

- Fork the project.
- Clone the forked project.
- Make your intended contributions to the project
- Create a branch and Push your local branch to your remote repository.
- Open a pull request to the develop branch of this repository.

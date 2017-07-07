# Progress Tracker
<i>progress_tracker</i> is an interactive commandline utility that
enables learners to keep track of their learning progress.

## Usage
    $ ./progress_tracker

## Collaboration
To set up the project for development, please follow the following
steps:

- TODO: Add chosen git workflow's steps here
- Create a Python 3 virtual environment, don't add your virtual
  environment directory to the repository
- Install [pip-tools](https://github.com/jazzband/pip-tools)
  into you virtual environment.
- Install project requirements with `$ pip-sync requirements.txt`

Note that to add a new project requirement:
- Add it to `requirements.txt` using the format in that file
- Run `pip-compile requirements.in`. To resolve dependencies and modify
  `requirements.txt`
- Run `$ pip-sync requirements.txt` to install the requirements.
- Add both `requirements.in` and `requirements.txt` in a commit.

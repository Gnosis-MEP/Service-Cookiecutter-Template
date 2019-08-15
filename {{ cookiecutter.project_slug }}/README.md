# {{ cookiecutter.project_name }}
{{ cookiecutter.description }}


# Installation

## Configure .env
Copy the `example.env` file to `.env`, and inside it replace `SIT_PYPI_USER` and `SIT_PYPI_PASS` with the correct information.

## Installing Dependencies

### Using pipenv
Run `$ pipenv shell` to create a python virtualenv and load the .env into the environment variables in the shell.

Then run: `$ pipenv install` to install all packages, or `$ pipenv install -d` to also install the packages that help during development, eg: ipython.
This runs the installation using **pip** under the hood, but also handle the cross dependency issues between packages and checks the packages MD5s for security mesure.


### Using pip
To install using pip directly, one needs to use the `--extra-index-url` when running the `pip install` command, in order for to be able to use our private Pypi repository.

To install from the `requirements.txt` file, run the following command, but replacing the `{SIT_PYPI_USER}` and `{SIT_PYPI_PASS}` with the correct values:
```
$ pip install -r --extra-index-url https://{SIT_PYPI_USER}:{SIT_PYPI_PASS}@sit-pypi.herokuapp.com/simple
```

## Install project as a local package
In order to be able to access the `{{ cookiecutter.package_name }}` python package from withing the python modules, one need to have it in the PYTHON_PATH.
The easiest way to do that is to install the project in editable mode, to do that run the following command inside the project root directory:
```
$ pip install -e .
```

# Running
Inside the python environment (virtualenv or conda environment), run:
```
$ ./{{ cookiecutter.package_name }}/.run.py
```

# Testing
Run the script `run_tests.sh`, it will run all tests defined in the **tests** directory.

Also, there's a python script at `./{{ cookiecutter.package_name }}/send_msgs_test.py` to do some simple manual testing, by sending msgs to the service stream key.


# Docker
## Build
Build the docker image using: `docker-compose build`

**ps**: It's required to have the .env variables loaded into the shell so that the container can build properly. An easy way of doing this is using `pipenv shell` to start the python environment with the `.env` file loaded.

## Run
Use `docker-compose run --rm service` to run the docker image


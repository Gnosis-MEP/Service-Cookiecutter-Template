# Service Cookiecutter Template
Use this to create new services


## Installing Cookiecutter
`$ pip install --user cookiecutter`, ref: [cookiecutter installation page](https://cookiecutter.readthedocs.io/en/latest/installation.html)

## Using this template

Run `$ cookiecutter https://github.com/Gnosis-MEP/Service-Cookiecutter-Template`


Then answer the questions related to the new service that's is being created.

In the end it will create a directory with the new project slug in the current directory.

# Whats inside

* Fully running service  skeleton
* Service configurations read from .env file
* Reading and processing `data` and `command` streams (event-sourcing paradigm for the latter)
* Simple python script for manualy sending test messages
* Unit tests setup and working test example
* Event tracing enabled (using Jaeger as distributed event tracing)
* Service Annoucement (optional)
* Documentation

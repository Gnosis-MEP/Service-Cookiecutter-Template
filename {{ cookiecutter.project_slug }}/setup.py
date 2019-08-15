from setuptools import setup

setup(
    name='{{ cookiecutter.package_name }}',
    version='0.1',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.author_email }}',
    packages=['{{ cookiecutter.package_name }}'],
    zip_safe=False
)

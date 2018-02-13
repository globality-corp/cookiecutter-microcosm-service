"""
Entrypoint module for WSGI containers.

"""
from {{ cookiecutter.project_name }}.app import create_app


app = create_app().app

"""
Entrypoint module for WSGI containers.

"""
# newrelic import must come before anything else to properly monitor application behavior
import newrelic.agent
newrelic.agent.initialize()

from {{cookiecutter.project_name}}.app import create_app  # noqa


app = create_app().app

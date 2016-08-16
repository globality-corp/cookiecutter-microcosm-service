"""
Entrypoint module for WSGI containers.

"""
{% if cookiecutter.enable_newrelic == True -%}
# newrelic import must come before anything else to properly monitor application behavior
import newrelic.agent
newrelic.agent.initialize(){% endif %}

from {{ cookiecutter.project_name }}.app import create_app  # noqa


app = create_app().app

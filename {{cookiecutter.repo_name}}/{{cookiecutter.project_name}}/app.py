"""
Create the application.

"""
from microcosm.api import create_object_graph
from microcosm.loaders import load_each, load_from_environ_as_json

from {{cookiecutter.project_name}} import postgres  # noqa
from {{cookiecutter.project_name}}.config import load_default_config
from {{cookiecutter.project_name}}.routes import example_routes  # noqa
from {{cookiecutter.project_name}}.stores import example_store  # noqa


def create_app(debug=False, testing=False):
    """
    Create the object graph for the application.

    """
    loader = load_each(
        load_default_config,
        load_from_environ_as_json,
    )

    graph = create_object_graph(
        name=__name__.split(".")[0],
        debug=debug,
        testing=testing,
        loader=loader,
    )

    graph.use(
        "discovery_convention",
        "example_routes",
        "health_convention",
        "postgres",
        "postgres_health_check",
        "sessionmaker",
        "session_factory",
        "swagger_convention",
    )

    return graph.lock()

"""
Create the application.

"""
from microcosm.api import create_object_graph
from microcosm.loaders import load_each, load_from_environ

from {{ cookiecutter.project_name }}.config import load_default_config
import {{ cookiecutter.project_name }}.postgres  # noqa
import {{ cookiecutter.project_name }}.routes.example.controller  # noqa
import {{ cookiecutter.project_name }}.routes.example.crud   # noqa
import {{ cookiecutter.project_name }}.stores.example_store  # noqa


def create_app(debug=False, testing=False, model_only=False):
    """
    Create the object graph for the application.

    """
    loader = load_each(
        load_default_config,
        load_from_environ,
    )

    graph = create_object_graph(
        name=__name__.split(".")[0],
        debug=debug,
        testing=testing,
        loader=loader,
    )

    graph.use(
        "example_store",
        "logging",
        "postgres",
        "sessionmaker",
        "session_factory",
    )

    if not model_only:
        graph.use(
            # conventions
            "build_info_convention",
            "discovery_convention",
            "health_convention",
            "port_forwarding",
            "postgres_health_check",
            # routes
            "example_routes",
            "swagger_convention",
        )

    return graph.lock()

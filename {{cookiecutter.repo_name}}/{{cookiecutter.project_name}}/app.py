"""
Create the application.

"""
from microcosm.api import create_object_graph
from microcosm.loaders.compose import load_config_and_secrets
from microcosm.loaders import load_each, load_from_environ, load_from_json_file
from microcosm_dynamodb.loaders.conventions import load_from_dynamodb

from {{ cookiecutter.project_name }}.config import load_default_config
import {{ cookiecutter.project_name }}.postgres  # noqa
import {{ cookiecutter.project_name }}.routes.example.controller  # noqa
import {{ cookiecutter.project_name }}.routes.example.crud   # noqa
import {{ cookiecutter.project_name }}.stores.example_store  # noqa


def create_app(debug=False, testing=False, model_only=False):
    """
    Create the object graph for the application.

    """
    config_loader = load_each(
        load_default_config,
        load_from_environ,
        load_from_json_file,
    )
    partitioned_loader = load_config_and_secrets(
        config=config_loader,
        secrets=load_from_dynamodb(),
    )

    graph = create_object_graph(
        name=__name__.split(".")[0],
        debug=debug,
        testing=testing,
        loader=partitioned_loader,
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
            "config_convention",
            "discovery_convention",
            "health_convention",
            "port_forwarding",
            "postgres_health_check",
            "swagger_convention",
            # routes
            "example_routes",
        )

    return graph.lock()

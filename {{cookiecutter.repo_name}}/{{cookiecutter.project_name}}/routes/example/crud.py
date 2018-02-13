"""
Example CRUD routes.

"""
from microcosm.api import binding
from microcosm_flask.conventions.base import EndpointDefinition
from microcosm_flask.conventions.crud import configure_crud
from microcosm_flask.operations import Operation
from microcosm_postgres.context import transactional

from {{ cookiecutter.project_name }}.resources.example_resources import (
    ExampleSchema,
    NewExampleSchema,
    SearchExampleSchema,
)


@binding("example_routes")
def configure_example_routes(graph):
    controller = graph.example_controller
    mappings = {
        Operation.Create: EndpointDefinition(
            func=transactional(controller.create),
            request_schema=NewExampleSchema(),
            response_schema=ExampleSchema(),
        ),
        Operation.Delete: EndpointDefinition(
            func=transactional(controller.delete),
        ),
        Operation.Replace: EndpointDefinition(
            func=transactional(controller.replace),
            request_schema=NewExampleSchema(),
            response_schema=ExampleSchema(),
        ),
        Operation.Retrieve: EndpointDefinition(
            func=controller.retrieve,
            response_schema=ExampleSchema(),
        ),
        Operation.Search: EndpointDefinition(
            func=controller.search,
            request_schema=SearchExampleSchema(),
            response_schema=ExampleSchema(),
        ),
    }
    configure_crud(graph, controller.ns, mappings)
    return controller.ns

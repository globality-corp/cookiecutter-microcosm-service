"""
Create example routes.

"""
from microcosm.api import binding, defaults
from microcosm_flask.conventions.base import EndpointDefinition
from microcosm_flask.conventions.crud import configure_crud
from microcosm_flask.conventions.crud_adapter import CRUDStoreAdapter
from microcosm_flask.operations import Operation
from microcosm_flask.namespaces import Namespace
from microcosm_flask.paging import PageSchema
from microcosm_postgres.context import transactional

from {{cookiecutter.project_name}}.models.example_model import Example
from {{cookiecutter.project_name}}.resources.example_resources import ExampleSchema, NewExampleSchema


@binding("example_routes")
@defaults(
    version="v1",
)
def configure_example_routes(graph):

    ns = Namespace(
        subject=Example,
        version=graph.config.example_routes.version,
    )
    adapter = CRUDStoreAdapter(graph, graph.example_store)

    mappings = {
        Operation.Create: EndpointDefinition(
            func=transactional(adapter.create),
            request_schema=NewExampleSchema(),
            response_schema=ExampleSchema(),
        ),
        Operation.Delete: EndpointDefinition(
            func=transactional(adapter.delete),
        ),
        Operation.Replace: EndpointDefinition(
            func=transactional(adapter.replace),
            request_schema=NewExampleSchema(),
            response_schema=ExampleSchema(),
        ),
        Operation.Retrieve: EndpointDefinition(
            func=adapter.retrieve,
            response_schema=ExampleSchema(),
        ),
        Operation.Search: EndpointDefinition(
            func=adapter.search,
            request_schema=PageSchema(),
            response_schema=ExampleSchema(),
        ),
    }

    configure_crud(graph, ns, mappings)

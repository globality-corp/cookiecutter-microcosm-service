"""
Create example routes.

"""
from microcosm.api import binding, defaults
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
    path_prefix="/v1",
)
def configure_example_routes(graph):

    ns = Namespace(
        subject=Example,
        path=graph.config.example_routes.path_prefix,
    )
    adapter = CRUDStoreAdapter(graph, graph.example_store)

    mappings = {
        Operation.Create: (
            transactional(adapter.create),
            NewExampleSchema(),
            ExampleSchema(),
        ),
        Operation.Delete: (
            transactional(adapter.delete),
        ),
        Operation.Replace: (
            transactional(adapter.replace),
            NewExampleSchema(),
            ExampleSchema(),
        ),
        Operation.Retrieve: (
            adapter.retrieve,
            ExampleSchema(),
        ),
        Operation.Search: (
            adapter.search,
            PageSchema(),
            ExampleSchema(),
        ),
    }

    configure_crud(graph, ns, mappings)

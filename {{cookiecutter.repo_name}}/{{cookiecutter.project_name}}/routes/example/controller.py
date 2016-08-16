"""
Example controller.

"""
from microcosm.api import binding
from microcosm_flask.conventions.crud_adapter import CRUDStoreAdapter
from microcosm_flask.namespaces import Namespace

from {{ cookiecutter.project_name }}.models.example_model import Example


@binding("example_controller")
class ExampleController(CRUDStoreAdapter):

    def __init__(self, graph):
        super(ExampleController, self).__init__(graph, graph.example_store)

        self.ns = Namespace(
            subject=Example,
            version="v1",
        )

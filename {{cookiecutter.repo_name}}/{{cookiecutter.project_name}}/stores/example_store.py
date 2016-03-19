"""
Example persistence.

"""
from microcosm.api import binding
from microcosm_postgres.store import Store

from {{cookiecutter.project_name}}.models.example_model import Example


class ExampleStore(Store):

    def retrieve_by_name(self, name):
        return self._retrieve(Example.name == name)


@binding("example_store")
def configure_example_store(graph):
    return ExampleStore(graph, Example)

"""
Example persistence.

"""
from microcosm.api import binding
from microcosm_postgres.store import Store

from {{ cookiecutter.project_name }}.models.example_model import Example


@binding("example_store")
class ExampleStore(Store):

    def __init__(self, graph):
        super().__init__(graph, Example)

    def retrieve_by_name(self, name):
        return self._retrieve(Example.name == name)

    def _filter(self, query, name=None, **kwargs):
        if name is not None:
            query = query.filter(
                Example.name == name,
            )
        return super()._filter(query, **kwargs)

    def _order_by(self, query, **kwargs):
        return query.order_by(
            Example.name.asc(),
        )

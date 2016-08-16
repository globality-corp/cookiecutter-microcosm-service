"""
Example resource matchers.

"""
from microcosm_flask.matchers import JSONMatcher
from {{ cookiecutter.project_name }}.resources.example_resources import ExampleSchema


class ExampleMatcher(JSONMatcher):
    @property
    def schema_class(self):
        return ExampleSchema

    def _matches(self, dct):
        return all((
            str(self.resource.id) == dct["id"],
            self.resource.name == dct["name"],
        ))


def matches_example(example):
    """
    Syntactic sugar for matching.

    """
    return ExampleMatcher(example)

"""
Example persistence tests.

Tests cover model-specific constraints under the assumption that framework conventions
handle most boilerplate.

"""
from hamcrest import (
    assert_that,
    calling,
    equal_to,
    is_,
    raises,
)
from microcosm_postgres.context import SessionContext, transaction
from microcosm_postgres.errors import DuplicateModelError

from {{ cookiecutter.project_name }}.app import create_app
from {{ cookiecutter.project_name }}.models.example_model import Example


class TestExamples(object):

    def setup(self):
        self.graph = create_app(testing=True)
        self.example_store = self.graph.example_store

        self.name = "NAME"

        self.context = SessionContext(self.graph)
        self.context.recreate_all()
        self.context.open()

    def teardown(self):
        self.context.close()
        self.graph.postgres.dispose()

    def test_create(self):
        """
        Examples can be persisted.

        """
        new_example = Example(
            name=self.name,
        )

        with transaction():
            self.example_store.create(new_example)

        retrieved_example = self.example_store.retrieve(new_example.id)
        assert_that(retrieved_example, is_(equal_to(new_example)))

    def test_create_duplicate(self):
        """
        Examples enforce uniqueness on type/external id.

        """
        example1 = Example(
            name=self.name,
        )
        example2 = Example(
            name=self.name,
        )

        with transaction():
            self.example_store.create(example1)

        assert_that(
            calling(self.example_store.create).with_args(example2),
            raises(DuplicateModelError),
        )

    def test_retrieve_by_name(self):
        """
        Examples can be retrieved by name.

        """
        new_example = Example(
            name=self.name,
        )

        with transaction():
            self.example_store.create(new_example)

        retrieved_example = self.example_store.retrieve_by_name(
            self.name
        )

        assert_that(retrieved_example, is_(equal_to(new_example)))

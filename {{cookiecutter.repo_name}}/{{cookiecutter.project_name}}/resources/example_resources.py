"""
Example resources.

"""
from marshmallow import Schema, fields
from microcosm_flask.linking import Link, Links
from microcosm_flask.namespaces import Namespace
from microcosm_flask.operations import Operation
from microcosm_flask.paging import PageSchema

from {{ cookiecutter.project_name }}.models.example_model import Example


class NewExampleSchema(Schema):
    name = fields.String(
        required=True,
    )


class ExampleSchema(NewExampleSchema):
    id = fields.UUID(
        required=True,
    )
    _links = fields.Method(
        "get_links",
        dump_only=True,
    )

    def get_links(self, obj):
        links = Links()
        links["self"] = Link.for_(
            Operation.Retrieve,
            Namespace(
                subject=Example,
                version="v1",
            ),
            example_id=obj.id,
        )
        return links.to_dict()


class SearchExampleSchema(PageSchema):
    name = fields.String()

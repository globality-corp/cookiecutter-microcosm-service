"""
Example resources.

"""
from marshmallow import fields, Schema

from microcosm_flask.linking import Links, Link
from microcosm_flask.operations import Operation

from {{cookiecutter.project_name}}.models.example_model import Example


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
        links["self"] = Link.for_(Operation.Retrieve, Example, example_id=obj.id)
        return links.to_dict()

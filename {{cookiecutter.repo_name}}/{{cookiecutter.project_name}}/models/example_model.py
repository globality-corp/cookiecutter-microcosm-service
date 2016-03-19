"""
An example model.

"""
from sqlalchemy import Column, String

from microcosm_postgres.models import EntityMixin, Model


class Example(EntityMixin, Model):
    """
    An example has a unique name.

    """
    __tablename__ = "example"

    name = Column(String, nullable=False, unique=True)

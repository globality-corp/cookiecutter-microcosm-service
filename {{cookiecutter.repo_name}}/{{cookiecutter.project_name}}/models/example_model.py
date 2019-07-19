"""
An example model.

"""
from microcosm_postgres.models import EntityMixin, Model
from sqlalchemy import Column, String


class Example(EntityMixin, Model):
    """
    An example has a unique name.

    """
    __tablename__ = "example"

    name = Column(String, nullable=False, unique=True)

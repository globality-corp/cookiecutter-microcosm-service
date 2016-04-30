"""
CLI entry points.

"""
from microcosm_flask.runserver import main as runserver_main
from microcosm_postgres.createall import main as createall_main
from microcosm_postgres.migrate import main as migrate_main

from {{cookiecutter.project_name}}.app import create_app


def createall():
    """
    Create (and possibly drop) database tables.

    """
    graph = create_app(debug=True, model_only=True)
    createall_main(graph)


def migrate():
    """
    Invoke Alembic migrations.

    """
    graph = create_app(debug=True, model_only=True)
    migrate_main(graph)


def runserver():
    """
    Invoke Flask development server.

    """
    graph = create_app(debug=True)
    runserver_main(graph)

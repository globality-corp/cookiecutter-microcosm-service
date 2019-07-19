"""
Integrate the web (Flask) and database (SQLAlchemy/Postgres) layers.

"""
from microcosm.api import binding
from microcosm_flask.session import register_session_factory
from microcosm_postgres.context import SessionContext
from microcosm_postgres.health import check_alembic, get_current_head_version


@binding("session_factory")
def configure_session_factory(graph):
    """
    Bind the SQLAlchemy session context to Flask.

    The current session is available at `g.db.session`.

    """
    return register_session_factory(graph, "db", SessionContext.make)


@binding("postgres_health_check")
def configure_postgres_health_check(graph):
    """
    Register the SQLAlchemy health check with the Flask health convention.

    """
    graph.health_convention.checks["database"] = check_alembic
    graph.health_convention.checks["database_migration_head"] = get_current_head_version

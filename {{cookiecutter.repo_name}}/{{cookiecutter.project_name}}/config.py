"""
Configure the application.

"""
from microcosm.configuration import Configuration


def load_default_config(metadata):
    """
    Construct application default configuration.

    There should be very little here.

    """
    config = Configuration(
        flask=dict(
            port={{cookiecutter.service_port}},
        ),
        logger=dict(levels=dict(override=dict(warn=[]))),
        swagger_convention=dict(version="v1"),
    )
    if metadata.testing:
        config.logger.levels.override.warn.append("alembic.runtime.migration")
    return config

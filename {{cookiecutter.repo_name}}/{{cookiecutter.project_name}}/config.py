"""
Configure the application.

"""


def load_default_config(metadata):
    """
    Construct application default configuration.

    There should be very little here.

    """
    if metadata.testing:
        warn = [
            "alembic.runtime.migration",
        ]
    else:
        warn = []

    config = dict(
        flask=dict(
            port={{ cookiecutter.service_port }},
        ),
        logging=dict(
            levels=dict(
                override=dict(
                    warn=warn,
                ),
            ),
        ),
        swagger_convention=dict(
            version="v1",
        ),
    )
    return config

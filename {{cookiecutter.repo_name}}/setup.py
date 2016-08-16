#!/usr/bin/env python
from setuptools import find_packages, setup

project = "{{ cookiecutter.project_name }}"
version = "{{ cookiecutter.project_version }}"

setup(
    name=project,
    version=version,
    description="{{ cookiecutter.short_description }}",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.author_email }}",
    url="https://github.com/{{ cookiecutter.organization_name }}/{{ cookiecutter.repo_name }}",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "microcosm>=0.10.0",
        "microcosm-flask>=0.16.2",
        "microcosm-logging>=0.5.0",
        "microcosm-postgres>=0.12.0",
        "ndg-httpsclient>=0.4.0",{% if cookiecutter.enable_newrelic == True %}
        "newrelic>=2.64.0.48",{% endif %}
        "uwsgi>=2.0.13.1",
    ],
    setup_requires=[
        "nose>=1.3.7",
    ],
    entry_points={
        "console_scripts": [
            "createall = {{ cookiecutter.project_name }}.main:createall",
            "migrate = {{ cookiecutter.project_name }}.main:migrate",
            "runserver = {{ cookiecutter.project_name }}.main:runserver",
        ],
    },
    tests_require=[
        "coverage>=3.7.1",
        "mock>=2.0.0",
        "PyHamcrest>=1.9.0",
    ],
)

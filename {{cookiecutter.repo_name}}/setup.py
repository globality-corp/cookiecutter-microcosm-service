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
        "microcosm>=2.1.0",
        "microcosm-dynamodb>=1.0.0",
        "microcosm-flask[metrics,spooky]>=1.4.0",
        "microcosm-logging>=1.0.0",
        "microcosm-postgres>=1.1.0",
        "pyOpenSSL>=17.5.0",
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

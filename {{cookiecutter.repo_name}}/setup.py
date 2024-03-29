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
        "microcosm>=2.12.0",
        "microcosm-flask[metrics,spooky]>=1.20.0",
        "microcosm-logging>=1.3.0",
        "microcosm-postgres>=1.19.0",
        "microcosm-secretsmanager>=1.1.0",
        "pyOpenSSL>=18.0.0",
    ],
    entry_points={
        "console_scripts": [
            "createall = {{ cookiecutter.project_name }}.main:createall",
            "migrate = {{ cookiecutter.project_name }}.main:migrate",
            "runserver = {{ cookiecutter.project_name }}.main:runserver",
        ],
    },
    extras_require={
        "test": [
            "coverage>=4.0.3",
        ],
    },
)

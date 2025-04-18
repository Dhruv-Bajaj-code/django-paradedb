from setuptools import setup, find_packages

setup(
    name='paradedb-django',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Django>=3.2',
        'psycopg2-binary',
        'pgvector'
    ],
    entry_points={
        'django.db.backends': [
            'paradedb=paradedb',
        ],
    },
)
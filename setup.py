from setuptools import setup, find_packages

setup(
    name='daos',
    version='0.0.49',
    packages=find_packages(),
    install_requires=[
        'SQLAlchemy==1.4.35',
        'psycopg2==2.9.3',
        'bs4~=0.0.1',
        'Inflector~=3.0.1'
    ]
)

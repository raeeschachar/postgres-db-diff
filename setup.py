import codecs
import os.path
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='postgres-db-diff',
    version='0.9',  # cause triggers, sequences are missing
    description='Command line tool to compare two PostgreSQL databases',
    long_description=long_description,
    url='https://github.com/petraszd/postgres-db-diff',
    author='Petras Zdanavičius',
    author_email='petraszd@gmail.com',

    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',

        # TODO: test if works
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.7',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='postgres comparison',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[],
    extras_require={
        'dev': [],
        'test': [],
    },

    # TODO: use this
    # entry_points={
        # 'console_scripts': [
            # 'sample=sample:main',
        # ],
    # },
)
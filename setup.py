# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_cython_demo']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'poetry-cython-demo',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': None,
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<3.11',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)

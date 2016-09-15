try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'ex47',
	'author': 'Hblee',
	'url': 'http://github.com/hblee12294',
	'author_email': 'hblee12294@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scipts': []
	'name': 'ex47'
}

setup(**config)
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'weathermajig',
    'author': 'Tyler Cipriani',
    'url': 'github.com/thcpiriani/weather-ma-jig',
    'author_email': 'tyler@tylercipriani',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['weathermajig'],
    'license': 'gpl-v2',

    'scripts': [],
    'name': 'weathermajig',
    'entry_points': {
        'console_scripts': [
            'weathermajig = weathermajig.main:main',
        ],
    },
}

setup(**config)
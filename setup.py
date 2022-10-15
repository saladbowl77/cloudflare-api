from setuptools import setup, find_packages

NAME = 'cl_api'
AUTHOR = 'saladbowl'

INSTALL_REQUIRES = [
    'requests>=2.27.1'
]

PACKAGES = [
    'cl_api'
]


setup(
    name='cl_api',
    version='1.0.0',
    maintainer=AUTHOR,
    install_requires=INSTALL_REQUIRES,
    packages=PACKAGES
)
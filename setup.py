from setuptools import setup

setup(
    url='https://github.com/blinklet/usermapper',
    author='Brian Linkletter',
    author_email='mail@brianlinkletter.ca',
    packages=['usermapper'],
    install_requires=['PyYAML'],
    version='0.1',
    license='GPLv3',
    description='An example of a python package from pre-existing code',
    long_description=open('README.md').read(),
)
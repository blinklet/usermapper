from setuptools import setup

setup(
    name='usermapper',

    url='https://github.com/blinklet/usermapper',
    author='Brian Linkletter',
    author_email='mail@brianlinkletter.ca',
    packages=['usermapper'],
    install_requires=['PyYAML'],
    version='0.3',
    license='GPLv3',
    description='Create a user-mappimg.xml file',
    long_description=open('README.md').read()
)
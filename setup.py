from setuptools import setup

setup(
    name='UserMapper',
    url='https://github.com/blinklet/usermapper',
    author='Brian Linkletter',
    author_email='mail@brianlinkletter.ca',
    packages=['usermapper'],
    install_requires=['PyYAML'],
    version='0.1',
    license='GPLv3',
    description='Create a user-mappimg.xml file',
    long_description=open('README.md').read()
)
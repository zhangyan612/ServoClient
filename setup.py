from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='ServoClient',
    version='0.1',
    author='', 
    author_email='zhangyan612@mail.com',
    packages=find_packages(),
    long_description=open('README.md').read()
)
# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='less-generator',
    version='0.1.0',
    description='Generator for serverless and headless projects',
    long_description=readme,
    author='Frank Rittinger',
    author_email='frank.rittinger@virtual-identity.com',
    url='https://github.com/frittinger/less-generator',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
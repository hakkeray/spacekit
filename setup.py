#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:copyright: (c) 2020 by Ru Keïn
:license: MIT, see LICENSE for more details.
"""

import os
import sys

from setuptools import setup
from setuptools.command.install import install

# circleci.py version
VERSION = "1.0.0"

def readme():
    """print long description"""
    with open('README.md') as f:
        return f.read()

class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)


setup(
    name="circleci",
    version=VERSION,
    description="Python wrapper for the CircleCI API",
    long_description=readme(),
    url="https://github.com/hakkeray/spacekit",
    author="Ru Keïn",
    author_email="hakkeray@gmail.com",
    license="MIT",
    keywords='spacekit spkt ml ai api sdk',
    packages=['spacekit'],
    install_requires=[
        'requests==2.18.4',
    ],
    python_requires='>=3',
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)


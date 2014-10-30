#!/usr/bin/env python

from pip.req import parse_requirements
from setuptools import setup

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt')

reqs = [str(ir.req) for ir in install_reqs]

setup(name="leonard",
      version="0.0.1",
      description="1951 Leonard Refrigerator Daemon",
      author="matt@nycresistor.com",
      author_email="matt@nycresistor.com",
      url="https://github.com/nycresistor/brewery/leonard",
      packages = ['leonard'],
      license = "LICENSE",
      install_requires=reqs
      )

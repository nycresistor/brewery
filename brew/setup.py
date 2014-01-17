#!/usr/bin/env python

from distutils.core import setup

setup(name='brew',
      version='0.0.1',
      description='NYC Resistor Brewery API',
      author='Matt Joyce',
      author_email='matt@nycresistor.com',
      url='http://brewery.nycresistor.com/api/',
      classifiers=[
          'Environment :: Brewery',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: NYC Resistor',
          'Intended Audience :: Brewery Regiment',
          'License :: Apache Software License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3'
          ],
      packages=['common', 'api', 'brew'],
      scripts=['bin/brew-master.py']
     )

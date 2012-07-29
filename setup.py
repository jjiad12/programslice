# coding: utf-8
from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='programslice',
      version=version,
      description="Static analysis tool for python",
      long_description="""\
Slice programs""",
      keywords='',
      author=u'Róman Joost',
      author_email='roman@bromeco.de',
      url='https://github.com/romanofski/programslice',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      extras_require=dict(
          test=['unittest2',
               ]
      ),
     )

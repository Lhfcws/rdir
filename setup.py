#!/usr/bin/python
# coding: utf-8
__author__ = 'lhfcws'

from setuptools import setup

setup(
      name="rdir",
      version="0.40",
      description="More powerful recursive dir. Support HTML pretty view in tree structure.",
      author="Lhfcws Wu",
      author_email="lhfcws@gmail.com",
      url="http://www.github.com/Lhfcws/rdir",
      license="MIT",
      packages= ["rdir"],
      scripts=["rdir/rdir.py"],
      install_requires=['colorama', 'pyquery'],
      keywords="dir doc"
)

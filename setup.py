#!/usr/bin/python
# coding: utf-8
__author__ = 'lhfcws'

from setuptools import setup, find_packages
setup(
      name="rdir",
      version="0.10",
      description="Recursively show modules' doc and structure",
      author="Lhfcws Wu",
      url="http://www.github.com/Lhfcws/rdir",
      license="LGPL",
      packages= find_packages(),
      scripts=["scripts/rdir.py"],
      )
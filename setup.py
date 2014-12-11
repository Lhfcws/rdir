#!/usr/bin/python
# coding: utf-8
__author__ = 'lhfcws'

from setuptools import setup

setup(
      name="rdir",
      version="0.20",
      description="Recursively show modules' doc and structure",
      author="Lhfcws Wu",
      author_email="lhfcws@gmail.com",
      url="http://www.github.com/Lhfcws/rdir",
      license="MIT",
      packages= ["rdir", "rdir/colorama"],
      scripts=["rdir/rdir.py"],
      )

#!/usr/bin/python
# coding: utf-8
__author__ = 'lhfcws'

from setuptools import setup

setup(
      name="rdir",
      version="0.30",
      description="Recursively show docs and structure of any object in the give module.",
      author="Lhfcws Wu",
      author_email="lhfcws@gmail.com",
      url="http://www.github.com/Lhfcws/rdir",
      license="MIT",
      packages= ["rdir"],
      scripts=["rdir/rdir.py"],
      install_requires=['colorama'],
      keywords="dir doc"
)

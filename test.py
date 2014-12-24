#!/usr/bin/python
# coding: utf-8
from rdir import rdir

__author__ = 'lhfcws'


<<<<<<< HEAD
name = urllib2.__name__

rdir(name, 1)
=======
rdir.rdir("urllib")
rdir.rdir(name="urllib", limit_deep=1)
rdir.rdir("urllib.urlopen")
rdir.rdir("urllib.urlopen", limit_deep=1)
>>>>>>> 3ee7355d87f0db6eadb6d47b31d847c5c822d424

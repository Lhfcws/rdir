#!/usr/bin/env python
# coding=utf-8

#	> File Name: generate_page.py
#	> Author: LY
#	> Mail: ly.franky@gmail.com
#	> Created Time: Sunday, December 14, 2014 AM09:40:42 CST

__author__ = 'laiy'

from pyh import *
import copy

class HTML_generator:
    def generate_HTML(self, deep, obj_name, parents, limit_deep):
        ''' Generate a local HTML file to make presentation more user-friendly 
        Separate two recursive methods to reduce the performance cost
        :param deep: int current
        :param obj_name: str param name of the object
        :param parents: list the parent chain in order
        :param limit_deep: int limit deep
        '''
        p = copy.deepcopy(parents)
        p.append(obj_name)

        full_name = self.get_full_name(p)



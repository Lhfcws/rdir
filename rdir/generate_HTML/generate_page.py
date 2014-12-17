#!/usr/bin/env python
# coding=utf-8

#	> File Name: generate_page.py
#	> Author: LY
#	> Mail: ly.franky@gmail.com
#	> Created Time: Sunday, December 14, 2014 AM09:40:42 CST

__author__ = 'laiy'

class HTML_generator:
    def generate_HTML(self, rdir_node):
        ''' Generate a local HTML file to make presentation more user-friendly 
        Separate two recursive methods to reduce the performance cost
        :param deep: int current
        :param obj_name: str param name of the object
        :param parents: list the parent chain in order
        :param limit_deep: int limit deep
        '''


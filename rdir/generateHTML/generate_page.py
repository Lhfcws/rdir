#!/usr/bin/env python
# coding=utf-8

#	> File Name: generate_page.py
#	> Author: LY
#	> Mail: ly.franky@gmail.com
#	> Created Time: Sunday, December 14, 2014 AM09:40:42 CST

__author__ = 'laiy'

import os
from pyquery import PyQuery

class HTMLGenerator:

    def __init__(self):
        pass

    def generate_tree_structure_HTML(self, rdir_node):
        with open(os.path.join(os.path.dirname(__file__), 'template', 'tree_template.html')) as f:
            self.template = PyQuery(f.read().decode('utf-8'))
        self.template('title').html(rdir_node.name)
        for key in rdir_node.list_children():
            self._add_node(rdir_node.get_children(key), 0)

    def _add_node(self, rdir_node, depth):
        self._add_node_to_HTML(rdir_node.name, rdir_node.doc, rdir_node.type, depth)
        for key in rdir_node.list_children():
            self._add_node(rdir_node.get_children(key), depth + 1)

    def _add_node_to_HTML(self, fullname, doc, obj_type, depth):
        pass


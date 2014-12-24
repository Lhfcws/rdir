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
        with open(os.path.join(os.path.dirname(__file__), 'template', 'tree_template.html')) as f:
            self.template = PyQuery(f.read().decode('utf-8'))
        with open(os.path.join(os.path.dirname(__file__), 'template', 'tree_node_template.html')) as f:
            self.node_template = PyQuery(f.read().decode('utf-8'))
        print(self.node_template.html())

    def generate_tree_structure_HTML(self, rdir_node):
        self.template('title').html(rdir_node.name)
        for key in rdir_node.list_children():
            self._add_node_recursively(rdir_node.get_children(key), 0)
        os.system(r'touch %s' % os.path.join(os.path.dirname(__file__), 'generatedHTML', rdir_node.name + '.html'))
        with open(os.path.join(os.path.dirname(__file__), 'generatedHTML', rdir_node.name + '.html'), 'w') as f:
            f.write(self.template.html())

    def _add_node_recursively(self, rdir_node, depth):
        self._add_node_to_HTML(rdir_node.name, rdir_node.doc, rdir_node.type[9 : -3], depth)
        for key in rdir_node.list_children():
            self._add_node_recursively(rdir_node.get_children(key), depth + 1)

    def _add_node_to_HTML(self, fullname, doc, obj_type, depth):
        node = self.node_template
        node('.tree_node').css('margin-left', str(depth * 50) + 'px')
        node('.interval').css('margin-left', str(depth * 50) + 'px')
        node('.node_fullname').html(fullname)
        node('.node_type').html(obj_type)
        node('.node_doc').html(doc)
        self.template('body').append(node.html())


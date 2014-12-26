#!/usr/bin/env python
# coding=utf-8
__author__ = 'laiy'

import os
import sys
from pyquery import PyQuery

reload(sys)
sys.setdefaultencoding('utf-8')


class HTMLGenerator(object):
    """HTML Generator
    """

    def __init__(self):
        with open(os.path.join(os.path.dirname(__file__), 'template', 'tree_template.html')) as f:
            self.template = PyQuery(f.read(), parser='html')
        with open(os.path.join(os.path.dirname(__file__), 'template', 'tree_node_template.html')) as f:
            self.node_template = PyQuery(f.read(), parser='html')

    def generate_tree_structure_HTML(self, root_node, output):
        """Generate a html file with tree structure.
        :param root_node: RDirNode root of the module
        """

        self.template('#header_text').html(root_node.name)
        self.template('title').html(root_node.name)
        for key in root_node.list_children():
            self._add_node_recursively(root_node.get_children(key), 0)
        # with open(os.path.join(os.path.dirname(__file__), 'generatedHTML', root_node.name + '.html'), 'w') as f:
        # use user defined output path
        with open(output, 'w') as f:
            f.write(self.template.html())

    def _add_node_recursively(self, rdir_node, depth):
        """Add node recursively to the views.
        :param rdir_node: RDirNode node to be added
        :param depth: int current recursive depth
        """
        self._add_node_to_HTML(rdir_node.name, rdir_node.doc, rdir_node.type[9 : -3], depth)
        for key in rdir_node.list_children():
            self._add_node_recursively(rdir_node.get_children(key), depth + 1)

    def _add_node_to_HTML(self, fullname, doc, obj_type, depth):
        """Add a DOM node to HTML template.
        :param fullname: str object full name like "urllib2.opener"
        :param doc: str object document
        :param obj_type: str object type
        :param depth: int current recursive depth
        """
        node = PyQuery(self.node_template.html())
        node('.tree_node').css('margin-left', str(depth * 50) + 'px')
        node('.interval').css('margin-left', str(depth * 50) + 'px')
        node('.node_fullname').html(fullname)
        node('.node_type').html(obj_type)
        if doc:
            node('.node_doc').html(doc.replace(' ', '&nbsp;').replace('\n', '<br/>') + '<br/>')
        else:
            node.remove('.node_doc')
        self.template('#wrapper').append(node.html())


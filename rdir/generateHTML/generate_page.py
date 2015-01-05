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

    def import_js(self):
        self.template("#script_jquery").attr("src", "%s/bin/js/jquery.min.js" % os.path.dirname(__file__))
        self.template("#script_rdir_tree").attr("src", "%s/bin/js/rdir_tree.js" % os.path.dirname(__file__))
        self.template("#script_jquery").html("var _lxml = 0;")
        self.template("#script_rdir_tree").html("var _lxml = 0;")

    def generate_tree_structure_HTML(self, root_node, output):
        """Generate a html file with tree structure.
        :param root_node: RDirNode root of the module
        :param output: Output html file
        """

        self.import_js()
        self.template('#header_name').html(root_node.name)
        self.template('#header_type').html(" &lt;%s&gt;" % root_node.type[7:-2])
        self.template('#header_doc').html(root_node.doc.
                                          replace('\t', '&nbsp;' * 4).
                                          replace(' ', '&nbsp;').
                                          replace('\n', '<br/>') + '<br/>')
        self.template('title').html(root_node.name)

        for key in root_node.list_children():
            self._add_node_recursively(root_node.get_children(key), 0)

        if len(root_node.list_children()) == 0:
            self._add_node_to_HTML("No visible children methods or members.",
                                   "If you see this, that means this object has nothing else to show.",
                                   "404",
                                   0)

        with open(output, 'w') as f:
            f.write(self.template.html())

    def _add_node_recursively(self, rdir_node, depth):
        """Add node recursively to the views.
        :param rdir_node: RDirNode node to be added
        :param depth: int current recursive depth
        """
        self._add_node_to_HTML(rdir_node.name, rdir_node.doc, rdir_node.type[7:-2], depth)
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
        node.add_class('tree_node')
        node('.tree_node').css('margin-left', str(depth * 50) + 'px')
        # node('.interval').css('margin-left', str(depth * 50) + 'px')
        node('.node_fullname').html(fullname)
        node('.node_type').html("&nbsp;&nbsp;Type&lt;%s&gt;" % obj_type)

        if doc:
            node('.node_doc').html(
                doc.replace('\t', '&nbsp;' * 4).replace(' ', '&nbsp;').replace('\n', '<br/>') + '<br/>')
        else:
            node.remove('.node_doc')

        self.template('#wrapper').append(node)


#!/usr/bin/env python
# coding=utf-8
__author__ = 'laiy'

import os
import sys
from pyquery import PyQuery
import multiprocessing

reload(sys)
sys.setdefaultencoding('utf-8')


class Util(object):
    """Util functions.
    """

    @staticmethod
    def split_jobs(job_list, pieces):
        l = len(job_list)
        unit = l / pieces
        remainder = l % pieces

        result = [None] * pieces
        start = 0
        for i in xrange(pieces):
            result[i] = job_list[start: start + unit]
            start += unit
        result[-1] += job_list[-remainder:]

        return tuple(result)


class HTMLGenerator(object):
    """HTML Generator
    """

    def __init__(self):
        self.MAX_WORKERS = 4
        self.MULTIPROCESS_BOUND = 20

    def load_tree_template(self):
        """Load tree HTML templates
        """
        with open(os.path.join(os.path.dirname(__file__), 'template', 'tree_template.html')) as f:
            self.template = PyQuery(f.read(), parser='html')
        with open(os.path.join(os.path.dirname(__file__), 'template', 'tree_node_template.html')) as f:
            self.node_template = PyQuery(f.read(), parser='html')
            self.node_template_html = self.node_template.html()

    def import_js(self, js_ids):
        """Import JS to HTML
        :param js_ids: dict type, {script_id with #: js_file_name}
                        exmaple: {"#script_jquery": "jquery.min.js"}
        """
        _path = os.path.dirname(__file__)

        for _id in js_ids.iterkeys():
            self.template(_id).attr("src", "%s/bin/js/%s" % (_path, js_ids[_id]))
            # In case that lxml change <script></script> to <script/>
            self.template(_id).html("var _lxml = 0;")

    def generate_tree_structure_HTML(self, root_node, output):
        """Generate a html file with tree structure.
        :param root_node: RDirNode root of the module
        :param output: Output html file
        """

        # Init
        self.load_tree_template()
        self.tree_nodes = []
        self.max_layer = 0

        self.import_js({
            # script_id : js_file_name
            "#script_jquery": "jquery.min.js",
            "#script_rdir_tree": "rdir_tree.js"
        })
        self.template('#header_name').html(root_node.name)
        self.template('#header_type').html(" &lt;%s&gt;" % root_node.type)

        header_doc = root_node.doc.replace('\t', '&nbsp;' * 4) \
            .replace(' ', '&nbsp;').replace('\n', '<br/>').strip()
        if len(header_doc) > 0:
            self.template('#header_doc').html(header_doc + '<br/>')
        else:
            self.template.remove('#header_doc')
        self.template('title').html(root_node.name)

        # Recur
        if len(root_node.list_children()) == 0:
            # self._add_node_to_HTML("No visible children methods or members.",
            #                        "If you see this, that means this object has nothing else to show.",
            #                        "404",
            #                        0)
            pass
        else:
            self.render_tree_html(root_node)


        # Render html
        for i in xrange(self.max_layer + 1):
            self.template("#choose_layer").append(
                "<option value='%d'>%d</option>" % (i, i)
            )

        self.template('#wrapper').append("\n".join(self.tree_nodes))

        # Write to file
        with open(output, 'w') as f:
            f.write(self.template.html())


    def render_tree_html(self, root_node):
        """ Render the node html. Use multiprocessing to speed up if needed.
        :param root_node: RDirNode root of the module
        """
        job_list = self.get_job_list(root_node)
        job_size = len(job_list)

        if job_size > self.MULTIPROCESS_BOUND:
            jobs_list = Util.split_jobs(job_list, self.MAX_WORKERS)
        else:
            jobs_list = [job_list]
        pool = multiprocessing.Pool(processes=self.MAX_WORKERS)

        result = []
        html = self.node_template.html()
        for jobs in jobs_list:
            if len(jobs) > 0:
                result.append(pool.apply_async(parse_tree_node_worker, (html, jobs)))

        # pool.close()
        # pool.join()

        self.tree_nodes = [None] * job_size
        for res in result:
            res = res.get()
            for tpl in res:
                index, node_html = tpl
                self.tree_nodes[index] = node_html


    def get_job_list(self, root_node):
        """Generate the job list
        :param root_node: RdirNode type, root of rdir_node
        :return: list type, [(index, rdir_node, depth)]
        """
        job_list = []
        for key in root_node.list_children():
            job_list += self.recur_node_to_list(root_node.get_children(key), 0)
        return [(index, job[0], job[1]) for index, job in enumerate(job_list)]

    def recur_node_to_list(self, rdir_node, depth):
        """Recursively traverse all the nodes into a sequential list.
        :param rdir_node:
        :param depth:
        :return: list type, [(rdir_node, depth)]
        """
        self.max_layer = (self.max_layer < depth) and depth or self.max_layer
        _list = [(rdir_node, depth)]
        for key in rdir_node.list_children():
            _list += self.recur_node_to_list(rdir_node.get_children(key), depth + 1)
        return _list


def parse_tree_node_worker(html, jobs):
    def __parse_tree_node(args):
        """Add a DOM node to HTML template.
        :param fullname: str object full name like "urllib2.opener"
        :param doc: str object document
        :param obj_type: str object type
        :param depth: int current recursive depth
        """
        index, rdir_node, depth = args

        node = node_template.clone()           # clone will be faster
        node.add_class('tree_node')
        node('.tree_node').css('margin-left', str(depth * 50) + 'px')
        node('.node_fullname').html(rdir_node.name)
        node('.node_type').html("&nbsp;&nbsp;Type&lt;%s&gt;" % rdir_node.type)

        if rdir_node.doc:
            node('.node_doc').html(
                rdir_node.doc.replace('\t', '&nbsp;' * 4).replace(' ', '&nbsp;').replace('\n', '<br/>') + '<br/>')
        else:
            node.remove('.node_doc')

        return index, str(node)

    node_template = PyQuery(html)

    result = []
    for job in jobs:
        result.append(__parse_tree_node(job))
    return result


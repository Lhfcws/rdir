#!/usr/bin/python
# coding: utf-8
"""Recursively show modules' doc and structure
"""
__author__ = 'lhfcws'

from core.rdir_core import RDirHandler
from generateHTML.generate_page import HTMLGenerator
import os

# Constants
WINDOW = 0

TERM = 0
JAVADOC = 1
TREE = 2
FILE = 3
RETURN = 4

SUFFIX_RDIR = ".rdir"
SUFFIX_HTML = ".html"


def rdir(name=None, limit_deep=2, mode=TERM, output=None):
    """Recursively show docs and structure of a object in the give module.

    Strongly suggest you to pass the value by using param name like `rdir(name="urllib")`.

    This method will ignore protected or private members which start with "_".
    Be aware, you can only assign either name or obj.
    If you assign both, rdir will just pick up name.

    Some enums in the module can be used like `rdir.TREE` or `rdir.WINDOW`.

    Args:
        name:   string type, full name invocation like "pyquery.PyQuery.eq" or module "pyquery"
        limit_deep: int type, search deep limit, default is 2. -1 for unlimited.
        mode:
                TERM: it'll print out to your terminal with color;
                FILE: it'll print out to a file without color;
                JAVADOC: it'll generate a Javadoc-style webpages;
                TREE: it'll generate a single webpage with tree structure to show the module;
                RETURN: it'll return an internal class RDirNode (not suggested).
        output: string type, The output file path. Only works in mode FILE, TREE, JAVADOC.
                    Default: current directory: '{$name}.rdir'.

    Returns:
        RETURN mode: Return a root node of RDirNode.
        Others: nothing return.
    """

    # Assertions
    assert (name is not None and name is not False) #or (obj is not None)

    # Internal functions
    def parse_output_2_html_suffix(_output, _name):
        if _output is None:
            return _name + SUFFIX_HTML
        elif not _output.endswith(SUFFIX_HTML):
            if _output.endswith("/"):
                _output += _name
            _output += SUFFIX_HTML
            return _output

        return _output

    # Init
    handler = RDirHandler()
    generator = HTMLGenerator()
    obj_name, parents = handler.parse_obj_name(name)
    # Identify ~ in path.
    if output.startswith("~"):
        output = os.path.expanduser(output)


    # Handle according with mode
    if mode == TERM:
        handler.recursive_dir_print(0, obj_name, parents, limit_deep)
    elif mode == RETURN:
        return handler.recursive_dir_return(0, obj_name, parents, limit_deep)
    elif mode == FILE:
        if output is None:
            output = name + SUFFIX_RDIR
        output = os.path.abspath(output)

        fp = open(output, "w")
        handler.recursive_dir_file(0, obj_name, parents, limit_deep, fp)
        fp.close()
    elif mode == JAVADOC:
        output = parse_output_2_html_suffix(output, name)
        output = os.path.abspath(output)

        root = handler.recursive_dir_return(0, obj_name, parents, limit_deep)
    elif mode == TREE:
        output = parse_output_2_html_suffix(output, name)
        output = os.path.abspath(output)

        root = handler.recursive_dir_return(0, obj_name, parents, limit_deep)
        generator.generate_tree_structure_HTML(root, output)
    else:
        print "Please input a valid mode.\n" + __doc__


#!/usr/bin/python
# coding: utf-8
"""Recursively show modules' doc and structure
"""
__author__ = 'lhfcws'

from core.rdir_core import RDirHandler

# Constants
TERM = 0
JAVADOC = 1
TREE = 2
RETURN = 4


def rdir(name=None, limit_deep=2, print_mode=TERM):
    """Recursively show docs and structure of any object in the give module.

    This method will ignore protected or private members which start with "_".

    Args:
        name: string type, full name invocation like "pyquery.PyQuery.eq" or module "pyquery"
        limit_deep: int type, search deep limit, default is 2. -1 for unlimited.
        print_mode:
                TERM: it'll print out to your terminal;
                JAVADOC: it'll generate a Javadoc-style webpages;
                TREE: it'll generate a single webpage with tree structure to show the module;
                RETURN: it'll return an internal class RDirNode (not suggested).
    Returns:
        RETURN mode: Return a root node of RDirNode.
        Others: nothing return.
    """
    assert name is not None and name is not False
    print "[rdir] Analyzing python object: " + name

    handler = RDirHandler()
    obj_name, parents = handler.parse_obj_name(name)

    if print_mode == TERM:
        handler.recursive_dir_print(0, obj_name, parents, limit_deep)
    elif print_mode == RETURN:
        return handler.recursive_dir_return(0, obj_name, parents, limit_deep)
    elif print_mode == JAVADOC:
        pass
    elif print_mode == TREE:
        pass


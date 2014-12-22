#!/usr/bin/python
# coding: utf-8
"""Recursively show modules' doc and structure
"""
__author__ = 'lhfcws'

import os
from core.rdir_core import RDirHandler

# Constants
TERM = 0
JAVADOC = 1
TREE = 2
RETURN = 4

def rdir(module, obj_full_name=None, limit_deep=2, print_mode=TERM):
    """Recursively show docs and structure of any object in the give module.

    This method will ignore protected or private members which start with "_".

    Args:
        module: string type, module.__name__ like "sys" or "pyquery"
                or now you can pass the module directly.
        obj_full_name: None if you want to see the whole module,
                or string type, full name invocation like "pyquery.PyQuery.eq"
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
    assert module is not None and module is not False
    assert obj_full_name is None or isinstance(obj_full_name, type(""))
    print "[rdir] Analyzing module: " + module

    mod_name = module
    if isinstance(module, type(os)):
        mod_name = module.__name__

    handler = RDirHandler()
    handler.import_module(mod_name)

    name = mod_name
    parents = []
    if obj_full_name is not None:
        name = obj_full_name
        parents = handler

    if print_mode == TERM:
        handler.recursive_dir_print(0, name, parents, limit_deep)
    elif print_mode == RETURN:
        return handler.recursive_dir_return(0, name, parents, limit_deep)
    elif print_mode == JAVADOC:
        pass
    elif print_mode == TREE:
        pass


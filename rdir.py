#!/usr/bin/python
# coding: utf-8
__author__ = 'lhfcws'

import copy

class __TempModule(object):
    def __init__(self):
        self.modules = {}

    def import_module(self, module_name):
        mod = __import__(module_name)
        self.modules[module_name] = mod


__temp_module = __TempModule()


def __line_prefix(num):
    return "-" * num


def __blank_prefix(num):
    return " " * num


def __get_doc(name, prefix):
    doc = eval(name + ".__doc__", __temp_module.modules)
    if doc is None:
        doc = ""
    else:
        doc = doc.replace("\n", "\n" + prefix)
    return doc


def __dir(name):
    return "dir(" + name + ")"


def __get_children(name):
    ls = eval(__dir(name), __temp_module.modules)
    res = filter(lambda child: not child.startswith("_"), ls)
    return res


def __get_full_name(paths):
    return ".".join(paths)


def __get_type(name):
    return " (" + str(eval("type(" + name + ")", __temp_module.modules)) + ")"


def __recursive_dir_with_doc(deep, mod_name, parents, limit_deep):
    line_prefix = __line_prefix(deep) + " "
    blank_prefix = __blank_prefix(deep) + " "
    p = copy.deepcopy(parents)
    p.append(mod_name)

    full_name = __get_full_name(p)

    output = line_prefix + mod_name + __get_type(full_name) + " :\n" + blank_prefix + __get_doc(full_name, blank_prefix)
    print output

    if deep == limit_deep:
        return

    children = __get_children(full_name)
    for child in children:
        __recursive_dir_with_doc(deep + 1, child, p, limit_deep)


def rdir(module, limit_deep=3):
    assert module is not None and module is not False
    assert type(module) == type(str())
    print "Parsing module: " + module

    __temp_module.import_module(module)
    deep = 0

    if type(module) == type(str()):
        __recursive_dir_with_doc(deep, module, [], limit_deep)
    else:
        raise Exception("Invalid param `module`, it should be a string or a module.")

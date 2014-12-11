#!/usr/bin/python
# coding: utf-8
"""Recursively show modules' doc and structure
"""
__author__ = 'lhfcws'

import copy as _copy

from colorama.ansi import Style as _Style, Fore as _Fore


class _TempModule(object):
    def __init__(self):
        self.modules = {}

    def import_module(self, module_name):
        mod = __import__(module_name)
        self.modules[module_name] = mod


_temp_module = _TempModule()


def _line_prefix(num):
    return "-" * num


def _blank_prefix(num):
    return " " * num


def _get_doc(name, prefix):
    doc = eval(name + ".__doc__", _temp_module.modules)
    if doc is None or type(doc) != type(str()):
        doc = ""
    else:
        doc = doc.replace("\n", "\n" + prefix)
    return doc


def _dir(name):
    return "dir(" + name + ")"


def _get_children(name):
    ls = eval(_dir(name), _temp_module.modules)
    res = filter(lambda child: not child.startswith("_"), ls)
    return res


def _get_full_name(paths):
    return ".".join(paths)


def _get_type(name):
    return " (" + str(eval("type(" + name + ")", _temp_module.modules)) + ")"


def _recursive_dir_with_doc(deep, mod_name, parents, limit_deep):
    line_prefix = _line_prefix(deep) + " "
    blank_prefix = _blank_prefix(deep) + " "
    p = _copy.deepcopy(parents)
    p.append(mod_name)

    full_name = _get_full_name(p)

    output = line_prefix + _prompt(_Fore.CYAN, mod_name) + _prompt(_Fore.BLUE, _get_type(full_name)) \
             + " :\n" + blank_prefix + _get_doc(full_name, blank_prefix)
    print output

    if limit_deep != -1 and deep == limit_deep:
        return

    children = _get_children(full_name)
    for child in children:
        _recursive_dir_with_doc(deep + 1, child, p, limit_deep)


def _prompt(color, string):
    prompt = color + _Style.BRIGHT + string + _Style.RESET_ALL
    return prompt


def rdir(module, limit_deep=2):
    """Recursively show module's doc and structure.
    TODO: More friendly way of presentation is coming soon.

    This method will ignore built-in arttribute which start with "_".

    Args:
        module: string type, module.__name__ like "sys" or "pyquery"
        limit_deep: int type, search deep limit, default is 3. -1 for unlimited.

    Returns:
        void.
        The content will be print to terminal.

    """
    assert module is not None and module is not False
    assert type(module) == type(str())
    print "[rdir] Analyzing module: " + module

    _temp_module.import_module(module)
    deep = 0

    _recursive_dir_with_doc(deep, module, [], limit_deep)

    # TODO(lhfcws) return a well-defined structure containing the result.
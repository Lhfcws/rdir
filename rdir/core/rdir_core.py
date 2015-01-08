#!/usr/bin/python
# coding: utf-8
__author__ = 'lhfcws'

# IMPORT
import copy
from colorama.ansi import Style, Fore
from rdir_node import RDirNode
import os

# CLASS


class ModuleSpace(object):
    """ The imported modules will be here.
    """

    def __init__(self):
        self.modules = {}

    def import_module(self, module_name):
        mod = __import__(module_name)
        self.modules[module_name] = mod


class RDirHandler(object):
    """ Core Handler
    """

    def __init__(self):
        self.builtin_types = [
            type(str()), type(test),
            type(RDirHandler.__init__),
            type(list()), type({}), type(set()),
            type({}.viewkeys), type(()), type(1),
            type(0.1), type(complex()), type(True),
            type(1L), type(None)
        ]
        self.builtin_types = [str(tp)[7:-2] for tp in self.builtin_types]
        self.context = ModuleSpace()

    @staticmethod
    def _line_prefix(num):
        return "-" * num

    @staticmethod
    def _blank_prefix(num):
        return " " * num

    @staticmethod
    def _prompt(color, string):
        """ Build the colorful prompt.
        :param color: Fore from colorama
        :param string: str string that needs changing color
        :return: str prompted string, it will show its color in the terminal.
        """
        prompt = color + Style.BRIGHT + string + Style.RESET_ALL
        return prompt

    @staticmethod
    def _dir(name):
        return "dir(%s)" % name

    @staticmethod
    def _get_full_name(paths):
        """ Get the full invocation name of the current param.
        :param paths: list parent path
        :return: str invocation format like grand_parent.parent.me
        """
        return ".".join(paths)

    def _is_module(self, name):
        return str(type(os))[7:-2] == self._get_type(name)

    def _is_builtin_type(self, typ):
        return self.builtin_types.count(typ) > 0

    def _get_submodules(self, name):
        if not self._is_module(name):
            return []

        submodules = []
        _module_paths = eval("%s.__path__" % name, self.context.modules)
        for _path in _module_paths:
            for file in os.listdir(_path):
                if not file.startswith("_") and file.endswith(".py"):
                    submodules.append(file.replace(".py", ""))
        return submodules

    def _get_doc(self, name, prefix):
        doc = eval(name + ".__doc__", self.context.modules)
        if doc is None or type(doc) != type(str()):
            doc = ""
        elif prefix is not None:
            doc = doc.replace("\n", "\n" + prefix)
        return doc

    def _get_children(self, name):
        ls = eval(self._dir(name), self.context.modules)
        res = filter(lambda child: not child.startswith("_"), ls)
        return res

    def _get_type(self, name):
        return (str(eval("type(%s)" % name, self.context.modules)))[7:-2]

    def parse_obj_name(self, name):
        names = name.split(".")
        self.context.import_module(names[0])
        return names[-1], names[:-1]

    def import_module(self, mod_name):
        self.context.import_module(mod_name)

    def recursive_dir_print(self, deep, obj_name, parents, limit_deep):
        """ Print the results to the terminal.
        Separate two recursive methods to reduce the performance cost
        :param deep: int current deep
        :param obj_name: str param name of the object
        :param parents: list the parent chain in order
        :param limit_deep: int limit deep
        """
        line_prefix = self._line_prefix(deep) + " "
        blank_prefix = self._blank_prefix(deep) + " "
        p = copy.deepcopy(parents)
        p.append(obj_name)

        full_name = self._get_full_name(p)
        typ = self._get_type(full_name)

        output = line_prefix + self._prompt(Fore.CYAN, obj_name) + \
                 self._prompt(Fore.BLUE, " (%s)" % typ) + " :\n" + \
                 blank_prefix + self._get_doc(full_name, blank_prefix)
        print output

        if self._is_builtin_type(typ):
            return

        if limit_deep != -1 and deep == limit_deep:
            return

        children = self._get_children(full_name)
        for child in children:
            self.recursive_dir_print(deep + 1, child, p, limit_deep)

    def recursive_dir_file(self, deep, obj_name, parents, limit_deep, fp):
        """ Print the results to a local file.
        Separate two recursive methods to reduce the performance cost
        :param deep: int current deep
        :param obj_name: str param name of the object
        :param parents: list the parent chain in order
        :param limit_deep: int limit deep
        :param fp: file handler
        """
        line_prefix = self._line_prefix(deep) + " "
        blank_prefix = self._blank_prefix(deep) + " "
        p = copy.deepcopy(parents)
        p.append(obj_name)

        full_name = self._get_full_name(p)
        typ = self._get_type(full_name)

        output = line_prefix + obj_name + " (%s)" % typ + " :\n" + blank_prefix + \
                 self._get_doc(full_name, blank_prefix)
        fp.write(output + "\n")

        if self._is_builtin_type(typ):
            return

        if limit_deep != -1 and deep == limit_deep:
            return

        children = self._get_children(full_name)
        for child in children:
            self.recursive_dir_file(deep + 1, child, p, limit_deep, fp)

    def recursive_dir_return(self, deep, obj_name, parents, limit_deep):
        """ Return the RDireNode object.
        Separate two recursive methods to reduce the performance cost
        :param deep: int current deep
        :param obj_name: str param name of the object
        :param parents: list the parent chain in order
        :param limit_deep: int limit deep
        :return: RDirNode root of the module.
        """
        p = copy.deepcopy(parents)
        p.append(obj_name)

        full_name = self._get_full_name(p)
        doc = self._get_doc(full_name, None)
        typ = self._get_type(full_name)

        children_nodes = {}
        continues = True

        if self._is_builtin_type(typ):
            continues = False

        if limit_deep != -1 and deep == limit_deep:
            continues = False

        if continues:
            children = self._get_children(full_name)
            for child in children:
                children_nodes[child] = self.recursive_dir_return(deep + 1, child, p, limit_deep)

        return RDirNode(full_name, doc, typ, children_nodes)


def test():
    pass
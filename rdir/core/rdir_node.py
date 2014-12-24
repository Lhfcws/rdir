#!/usr/bin/python
# coding: utf-8
__author__ = 'lhfcws'


class RDirNode(object):
    """ Node of rdir dict.
    This is a immutable class.
    """

    def __init__(self, fullname, doc, obj_type, children):
        """ Init
        :param name: object full name like "urllib2.opener"
        :param doc: object document
        :param obj_type: object type
        :param children: object's sub-objects
        """
        assert isinstance(fullname, type(""))
        assert isinstance(children, type({}))

        self.name = fullname
        self.doc = doc
        if isinstance(obj_type, type("")):
            self.type = obj_type
        else:
            self.type = str(obj_type)

        self.children = children

    def count_children(self):
        """ Size of the children.
        :return: int size of the children
        """
        return len(self.children)

    def list_children(self):
        """ List the keys of self.children
        :return: list [sub-object's name]
        """
        return self.children.keys()

    def get_children(self, key):
        """ Get a child node by a given key
        :param key: str sub-object's name
        :return: RDirNode node of the sub-object
        """
        assert isinstance(key, type(""))
        return self.children[key]

    def get_name(self):
        """ Get the object's own name.
        :return: str var name
        """
        return self.name.split(".")[-1]

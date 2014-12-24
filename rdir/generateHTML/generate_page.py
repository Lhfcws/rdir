#!/usr/bin/env python
# coding=utf-8

#	> File Name: generate_page.py
#	> Author: LY
#	> Mail: ly.franky@gmail.com
#	> Created Time: Sunday, December 14, 2014 AM09:40:42 CST

__author__ = 'laiy'

class HTMLGenerator:
    def generate_java_doc(self, rdir_node):
        children_keys = rdir_node.list_children()
        for key in children_keys:
            children = rdir_node.get_children(key)
            print(children.get_name())


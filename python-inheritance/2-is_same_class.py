#!/usr/bin/python3
"""Function that checks exact class of object"""


def is_same_class(obj, a_class):
    """Return True if obj is exactly instance of a_class"""
    return obj.__class__ is a_class

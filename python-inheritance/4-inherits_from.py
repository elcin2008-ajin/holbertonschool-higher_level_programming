#!/usr/bin/python3
"""Function that checks inheritance but not same class"""


def inherits_from(obj, a_class):
    """Return True if obj is instance of a subclass of a_class"""
    return isinstance(obj, a_class) and type(obj) is not a_class

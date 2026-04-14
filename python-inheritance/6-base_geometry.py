#!/usr/bin/python3
"""BaseGeometry class with unimplemented area method"""


class BaseGeometry:
    """Geometry base class"""

    def area(self):
        """Raises Exception because area is not implemented"""
        raise Exception("area() is not implemented")

#!/usr/bin/python3
"""Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square defined by a single size"""

    def __init__(self, size):
        """Initialize square with size"""

        self.integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)

    def __str__(self):
        """String representation of square"""
        return f"[Rectangle] {self.__size}/{self.__size}"

#!/usr/bin/python3
""""Module of updated Square with getter and setter"""


class Square:
    """class Square with private attribute size w prop and setter"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """method to get value of size"""
        return self.__size

    @size.setter
    def size(self, size):
        """method to set value of size"""
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")

    def area(self):
        """Public instance method to determine area"""
        return int(self.__size) * int(self.__size)

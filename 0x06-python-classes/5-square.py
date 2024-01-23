#!/usr/bin/python3
"""Module for class Square"""


class Square:
    """class Square with private size, public ins method area and print"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Method to get value of size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Method to set value of size"""
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")

    def area(size):
        """Public instance method to determine area"""
        return int(self.__size) * int(self.__size)

    def my_print(self):
        """Public instance method to print square to stdout with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(int(self.__size)):
                for i in range(int(self.__size)):
                    print("#", end="")
                print()

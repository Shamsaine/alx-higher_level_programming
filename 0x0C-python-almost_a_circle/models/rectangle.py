#!/usr/bin/python3

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super()__init__(self, id=None):
            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y
    def __str__(self):
        return 

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = y

    def area(self):
        pass

    def display(self):
        pass

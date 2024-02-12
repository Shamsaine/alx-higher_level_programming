#!/usr/bin/python3

class Base:
    """This class will be the “base” of all other classes
    
    The goal of it is to manage id attribute in all your future classes
    
    and to avoid duplicating the same code (by extension, same bugs)

    """

    __nb_objects = 0

    def __init__(self, id = None):
        """this is the class constructor

        where new bases are initialized

        Args:
            id: idenity of the new base

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

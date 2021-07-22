import os


class Figure:
    name = os.path.basename(__file__)[:-3]

    def __init__(self, a, b=None, c=None, ):
        if self.__class__ == Figure:
            raise ValueError("abstract method use is not desirable")
        self.a: int = a
        self.b: int = b
        self.c: int = c

    def add_area(self, arg):
        if not isinstance(arg, Figure):
            raise ValueError("Does not inherit from the class Figure")

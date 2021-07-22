import os

from src.Rectangle import Rectangle


class Square(Rectangle):
    name = os.path.basename(__file__)[:-3]

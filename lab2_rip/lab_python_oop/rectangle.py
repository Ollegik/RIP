from lab_python_oop.figures import Figure
from lab_python_oop.color import FColor


class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, width_param, height_param):
        self.width = width_param
        self.height = height_param
        self.fc = FColor()
        self.fc.colorproperty = color_param

    def square(self):
        return self.width*self.height

    def __repr__(self):
        return '{} {} цвета, шириной {}, высотой {} и площадью {}.'.format(
            Rectangle.get_figure_type(),
            self.fc.colorproperty,
            self.width,
            self.height,
            self.square()
        )
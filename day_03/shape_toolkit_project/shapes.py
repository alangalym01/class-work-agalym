import math

class Rectangle:
    """
    A rectangle shape defined by width and height.

    Attributes:
        width (int): how wide the rectangle is
        height (int): how tall the rectangle is
    """

    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    def area(self) -> int:
        """
        Calculate the are of the rectangle
        Returns:
            int: area (width * height)
        """
        return self.width * self.height

    def describe(self) -> None:
        """
        Print a description of the rectangle
        """
        print(f"This rectangle is {self.height} cm long and {self.width} cm wide, and has an area of {self.area()} cm^2")

class Circle:
    """
    A rectangle shape defined by width and height.

    Attributes:
        radius (int): radius of the circle
    """

    def __init__(self, radius: int):
        self.radius = radius

    def area(self) -> int:
        """
        Calculate the are of the rectangle
        Returns:
            int: area (pi * radius**2)
        """
        return math.pi * self.radius**2

    def describe(self) -> None:
        """
        Prints a description of the rectangle

        Returns:
            None
        """
        print(f"This circle has a radius of {self.radius} cm and an area of {self.area()} cm^2")

class Triangle:
    def __init__(self, height: int, base: int):
        self.height = height
        self.base = base

    def area(self) -> int:
        """
        Calculate the are of the rectangle
        Returns:
            int: area (height * base * 0.5)
        """
        return self.height * self.base * 0.5

    def describe(self) -> None:
        """
        Print a description of the triangle.

        Returns
            None
        """
        print(f"This triangle has a base of {self.base} cm, a height of {self.height} cm, and an area of {self.area()} cm^2")
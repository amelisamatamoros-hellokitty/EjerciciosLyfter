from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass
        

class Circle(Shape):

    def __init__(self,radius):
        self.radius=radius

    def calculate_perimeter(self):
        perimeter=2*pi*self.radius
        return perimeter

    def calculate_area(self):
        area=pi*self.radius**2
        return area      


class Rectangle(Shape):

    def __init__(self,height,width):
        self.height=height
        self.width=width

    def calculate_perimeter(self):
        perimeter=2*(self.width+self.height)
        return perimeter

    def calculate_area(self):
        area=self.height*self.width
        return area 
    
class Square(Rectangle):

    def __init__(self,side):
        super().__init__(side,side)


    
my_circle=Circle(5)
print(my_circle.calculate_area())
print(my_circle.calculate_perimeter())
my_square=Square(6)
print(my_square.calculate_area())
print(my_square.calculate_perimeter())
my_rectangle=Rectangle(4,5)
print(my_rectangle.calculate_area())
print(my_rectangle.calculate_perimeter())

my_shape=Shape()

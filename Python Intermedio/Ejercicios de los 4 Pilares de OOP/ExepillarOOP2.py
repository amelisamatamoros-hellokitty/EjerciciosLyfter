from math import pi

class Shape:

    def calculate_perimeter(self):
        print("This is the parent's class method to calculate the perimeter")

    def calculate_area(self):
        print("This is the parent's class method to calculate the area")
        

class Circle(Shape):

    def __init__(self,radius):
        self.radius=radius

    def calculate_perimeter(self):
        perimeter=2*pi*self.radius
        return perimeter

    def calculate_area(self):
        area=pi*self.radius**2
        return area      


class Square(Shape):

    def __init__(self,height,width):
        self.height=height
        self.width=width

    def calculate_perimeter(self):
        perimeter=2*(self.width+self.height)
        return perimeter

    def calculate_area(self):
        area=self.height*self.width
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

my_circle=Circle(5)
print(my_circle.calculate_area())
print(my_circle.calculate_perimeter())
my_square=Square(6,6)
print(my_square.calculate_area())
print(my_square.calculate_perimeter())
my_rectangle=Rectangle(4,5)
print(my_rectangle.calculate_area())
print(my_rectangle.calculate_perimeter())

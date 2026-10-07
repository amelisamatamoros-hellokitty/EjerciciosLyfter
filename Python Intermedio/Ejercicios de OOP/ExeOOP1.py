import math

class Circle:
    
    def __init__(self,radius):
        self.radius=radius

    def get_area(self,radius):
        area=math.pi*(self.radius**2)
        return area

radius_1=Circle(float(input("Enter a radius in meters for the circle:  ")))
print(f"The circle's area in square meters is {radius_1.get_area(radius_1.radius)}")

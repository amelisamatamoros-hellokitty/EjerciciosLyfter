class Rectangle:

    def __init__(self,width,height):
        self.width=width
        self.height=height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        try:
            value=int(value)
        except:
            raise TypeError("Height and Width must be numbers")
        if value<0:
            raise ValueError("The width can't be a negative number")
        
        self._width=value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        try:
            value=int(value)
        except:
            raise TypeError("Height and Width must be numbers") 
        if value<0:
            raise ValueError("The height can't be a negative number")
        
        self._height=value


    def get_area(self):
        area=self.width*self.height
        return area

    def get_perimeter(self):
        perimeter=(2*self.width)+(2*self.height)
        return perimeter

def main():
    while True:    
        try:
            my_rectangle=Rectangle(input("Enter the width:  "),input("Enter the height:  "))
            break        
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
    return my_rectangle

rectangle_1=main()
print(rectangle_1.get_area())
print(rectangle_1.get_perimeter())


class Rectangle:

    def __init__(self,width,height):
        self.width=width
        self.height=height

    def get_area(self):
        area=self.width*self.height
        return area

    def get_perimeter(self):
        perimeter=(2*self.width)+(2*self.height)
        return perimeter

def verify_width():
    while True:
        try:
            width_1=int(input("Enter the width:  "))
            if width_1>0:
                return width_1
            else:
                print("Submit a number that's greater then zero")   
        except ValueError as e:
            print("You submitted a parameter that's different than a number")

def verify_height():
    while True:
        try:    
            height_1=int(input("Enter the height:  "))
            if height_1>0:
                return height_1
            else:
                print("Submit a number that's greater then zero")            
        except ValueError as e:
                print("You submitted a parameter that's different than a number")


my_width=verify_width()
my_height=verify_height()
rectangle_1=Rectangle(my_width,my_height)
print(rectangle_1.get_area())
print(rectangle_1.get_perimeter())


#Create a class Rectangle with private attributes length and width.Overload '<' operator to compare the area of 2 rectangles
class Rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width

    def area(self):
        return (self.__length * self.__width)

    def __lt__(self, other):
        return self.area() < other.area()

length1 = int(input("Enter the length of first rectangle : "))
width1 = int(input("Enter the width of first rectangle : "))
rectangle1=Rectangle(length1,width1)

length2 = int(input("Enter the length of second rectangle : "))
width2 = int(input("Enter the width of second rectangle : "))
rectangle2=Rectangle(length2,width2)

# r1=Rectangle(4,5)
# r2=Rectangle9(6,3)

if rectangle1 < rectangle2:
    print("Area of rectangle 1 is small")
else:
    print("Area of rectangle 2 is small")


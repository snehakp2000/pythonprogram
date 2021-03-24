#Create Rectangle class with attributes length and breadth and methods to find area and perimeter.
#Compare two Rectangle objects by their area.
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return (self.length*self.breadth)
    def perimeter(self):
        return (2*(self.length+self.breadth))
r1=Rectangle(4,5)
r2=Rectangle(9,2)
a1=r1.area()
p1=r1.perimeter()
a2=r2.area()
p2=r2.perimeter()
print("Area of first rectangle is",a1)
print("Area of second rectangle is",a2)
print("Perimeter of first rectangle is",p1)
print("Perimeter of second rectangle is",p2)

if a1>a2:
    print("Area of rectangle 1 is greater than area of rectangle 2")
else:
    print("Area of rectangle 2 is greater than area of rectangle 1")

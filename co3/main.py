from Graphics import Circle, Rectangle
from Graphics.ThreeDgraphics.Cuboid import *
from Graphics.ThreeDgraphics import Sphere as s

r = int(input("Enter the radius:"))
print("Area of the given circle=", Circle.area(r))
print("Perimeter of the given circle=", Circle.perimeter(r))
print("____________________________________________________")

l = int(input("\nEnter length of the rectangle:"))
b = int(input("Enter the breadth of the rectangle:"))
print("Area of the given rectangle=", Rectangle.area(l, b))
print("Perimeter of the given rectangle=", Rectangle.perimeter(l, b))
print("____________________________________________________")

l = int(input("\nEnter length of the cuboid:"))
b=int(input("Enter breadth of the cuboid:"))
h=int(input("Enter height of the cuboid:"))
print("Area of the given cuboid=", area(l, b, h))
print("Perimeter of the given cuboid=", perimeter(l, b, h))
print("____________________________________________________")

r = int(input("\nEnter the radius of the sphere:"))
print("Area of the given sphere=", s.area(r))
print("Perimeter of the given circle=", s.perimeter(r))
print("___________________________________________________")

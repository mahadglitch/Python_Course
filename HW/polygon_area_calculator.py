from abc import ABC, abstractmethod

# Abstract base class
class Polygon(ABC):

    @abstractmethod
    def area(self):
        pass


# Child class: Rectangle
class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Child class: Square
class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# Child class: Triangle
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# -------- Main Program --------
print("Polygon Area Calculator")
print("1. Rectangle")
print("2. Square")
print("3. Triangle")

choice = int(input("Choose a polygon (1-3): "))

if choice == 1:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    shape = Rectangle(l, w)

elif choice == 2:
    s = float(input("Enter side: "))
    shape = Square(s)

elif choice == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    shape = Triangle(b, h)

else:
    print("Invalid choice")
    exit()

print("Area =", shape.area())

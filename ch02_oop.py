""" 4 Pillars of OOP
Encapsulation - 1. Objects group variables, which hold state, and methods that alter state, in a single unit
2. Hiding a class' internal data to prevent the client from directly accessing it.
Code outside of class that uses the object is the client.
Python does not have private variables if variable starts with underscore self._unsafe = "unsafe" self.public = "safe"
Abstraction - reduce to essential characteristics
Polymorphism - present same interface for different data types
Inheritance - Classes can inherit methods and variables from another class
"""


# Polymorphism
print("Hello World")
print(200)
print(200.1)


class Shape:

    def what_am_i(self):
        print("I am a shape!")

    def area(self):
        return self.width * self.length


class Rectangle(Shape):
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.length = l
        self.recs.append((self.width, self.length))

    def calculate_perimeter(self):
        print(2 * self.width + 2 * self.length)

    def print_size(self):
        print("""Rectangle: {} by {}""".format(self.width, self.length))


class Square(Shape):
    def __init__(self, s):
        self.s = s

    def calculate_perimeter(self):
        return self.s *4

    def change_size(self, new_size):
        self.s += new_size

    def print_size(self):
        print("""Square: {} by {}""".format(self.s, self.s))


class Triangle(Shape):
    def calculate_perimeter(self):
        print(self.side_a + self.side_b + self.side_c)

    def print_size(self):
        print("""Triangle: {} by {} by {}""".format(self.side_a, self.side_b, self.side_c))


a_rectangle = Rectangle(10, 5)
a_rectangle.print_size()
a_rectangle.calculate_perimeter()

b_rectangle = Rectangle(17, 8)
c_rectangle = Rectangle(9,11)
a_rectangle.what_am_i()
print(Rectangle.recs)

a_square = Square(8)
a_square.what_am_i()
a_square.print_size()
a_square.calculate_perimeter()
a_square.change_size(-1)
a_square.calculate_perimeter()
a_square.print_size()

a_triangle = Triangle(5, 7, 13)
a_triangle.calculate_perimeter()
a_triangle.print_size()
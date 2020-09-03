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
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def area(self):
        return self.width * self.length

    def print_size(self):
        print("""{} by {}""".format(self.width, self.length))

class Rectangle(Shape):
   pass

class Square(Shape):
    pass


a_rectangle = Rectangle(10,5)
a_rectangle.print_size()
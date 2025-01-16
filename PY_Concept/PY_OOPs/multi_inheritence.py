class A:
    def method_a(self):
        return "Method A"

class B:
    def method_b(self):
        return "Method B"

class C(A, B):
    def method_c(self):
        return "Method C"

# Creating instances
c = C()
print(c.method_a())  # Output: Method A
print(c.method_b())  # Output: Method B
print(c.method_c())  # Output: Method C

class A:
    def method(self):
        return "Method A"

class B(A):
    def method(self):
        return super().method() + ", Method B"

# Creating instances
b = B()
print(b.method())  # Output: Method A, Method B

class Circle:
    pi = 3.14159

    @classmethod
    def area(cls, radius):
        return cls.pi * radius ** 2

# Using the class method
print(Circle.area(5))  # Output: 78.53975

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

# Creating an instance
circle = Circle(5)
print(circle.diameter)  # Output: 10

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# Creating instances
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(f"({p3.x}, {p3.y})")  # Output: (4, 6)




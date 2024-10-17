class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


point1 = Point(5, 9)
point2 = Point(3, 5)

result = point1 + point2
print("Wynik:", result)  # Wynik: Point(8, 14)

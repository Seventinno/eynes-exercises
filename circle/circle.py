import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
        if self.radius <= 0:
            raise ValueError("El radio debe ser mayor a 0")

    def get_radius(self):
        return self.radius

    def set_radius(self,radius):
        if radius <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        perimetro = 2 * math.pi * self.radius

        return perimetro

    def __mul__(self, n):
        if n <= 0:
            raise ValueError("El número de multiplicación debe ser mayor que 0")
        return Circle(self.radius * n)

    def __str__(self):
        return f"Circulo con radio {self.radius}"

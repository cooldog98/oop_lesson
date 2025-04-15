import math
import copy

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt((self.x**2) + (self.y**2))

    def __str__(self):
        return f'Vector(x={self.x}, y={self.y})'

    def dot(self, v):
        return self.x*v.x + self.y*v.y

    def add(self, v): # u.add(v)
        return Vector(self.x+v.x, self.y+v.y)

    def subtract(self, v):
        return Vector(self.x-v.x, self.y-v.y)

    def multiply(self, s):
        return Vector(s*self.x, s*self.y)

    def __eq__(self, other):# vector = vector
        return self.x == other.x and self.y == other.y

    def __add__(self, other):# vector + vector
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):# vector - vector
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):# similar with __str__ but ครอบคุมมากกว่า อธิบายไม่ถูก แต่ใช้อันนี้ดีกว่า
        return f'Vector(x={self.x}, y={self.y})'

    def __mul__(self, num): # vector * vector
        return Vector(self.x * num, self.y * num)

    def __rmul__(self, num): # num * vector
        return self.__mul__(num)



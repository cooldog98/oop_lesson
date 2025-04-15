# import math
# import copy
#
# class Vector:
#     """ Define a vector in 2D space """
#
#     def __init__(self, x=0, y=0):
#         # assign __x and __y via their properties for input validation
#         self.x = x
#         self.y = y
#
#     # all methods from previous exercises already defined here, but hidden
#
#     # insert your new method(s) here (don't forget the indentation)
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, new_x):
#         if not isinstance(new_x, (int, float)):
#             raise TypeError('x must be a number')
#         self.__x = new_x
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, new_y):
#         if not isinstance(new_y, (int, float)):
#             raise TypeError('y must be a number')
#         self.__y = new_y

from vector import Vector

# class Border:
#     def __init__(self, corner, width, height):
#         self.corner = corner
#         self.width = width
#         self.height = height
#
#     def __repr__(self):
#         return (f"Border(corner={self.corner},"
#                 f" width={self.width}, height={self.height})")
#
#     @property
#     def corner(self):
#         return self._corner
#
#     @corner.setter
#     def corner(self, new_corner):
#         if isinstance(new_corner, str):
#             raise TypeError('corner must be a Vector object')
#         self._corner = new_corner
#
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, new_width):
#         if isinstance(new_width, str):
#             raise TypeError('width must be a number')
#         if 0 >= new_width:
#             raise ValueError('width must be greater than zero')
#         self._width = new_width
#
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self, new_height):
#         if isinstance(new_height, str):
#             raise TypeError('height must be a number')
#         if 0 >= new_height:
#             raise ValueError('height must be greater than zero')
#         self._height = new_height

# self.x = Toy everyone can play with.
# self._x = Toy with a "Please don’t touch" sign.
# self.__x = Toy locked in a secret box! 🎁


import math

# class Container:
#     ''' This is a meta class that's supposed to NOT have an initializer.
#         It's only to be extended upon.
#     '''
#     def __init__(self):
#         pass
#
# class Box(Container):
#     ''' A cuboid box, having width, depth, and height.
#         When initializing the dimensions should be in cm.
#         The dimcost is the sum of all three sides.
#     '''
#     def __init__(self, width, depth, height):
#         self.width = width
#         self.depth = depth
#         self.height = height
#         self.dim_cost = width + depth + height
#         self.volume = width * depth * height
#
# class Cylinder(Container):
#     ''' A cylindrical tube, having length and diameter.
#         It is used for shipping long things like rolled posters.
#         Both dimensions should be in cm.
#     '''
#     def __init__(self, length, diameter):
#         self.length = length
#         self.diameter = diameter
#         self.dim_cost = pi * diameter
#         self.volume = pi * (diameter / 2) ** 2
#
# mybox = Box(10, 10, 10)
# mybox.volume = 300
# print(mybox.width, mybox.depth, mybox.height, mybox.volume)


# import math
#
#
# class Container:
#     """ This is a meta class that's supposed to NOT have an initializer.
#         It's only to be extended upon.
#     """
#
#     def __init__(self):
#         pass
#
#
# class Mushroom(Container):
#     """ A mushroom-shaped container having a stem and a cap.
#         Cap radius must be LARGER than the stem radius.
#         If the user tries to make the cap too small, must throw ValueError.
#         Dim Cost is: (length of stem) + (diameter of cap)
#         Volume is: (volume of stem) + (volume of cap)
#     """
#
#     def __init__(self, stem_diameter, stem_length, cap_diameter):
#         if cap_diameter <= stem_diameter:
#             raise ValueError
#         if min(stem_diameter, stem_length, cap_diameter) <= 0:
#             raise ValueError
#         self.__stem_diameter = stem_diameter
#         self.__stem_length = stem_length
#         self.__cap_diameter = cap_diameter
#
#     @property
#     def stem_diameter(self):
#         return self.__stem_diameter
#
#     @stem_diameter.setter
#     def stem_diameter(self, stem_diameter):
#         if self.__cap_diameter <= stem_diameter:
#             raise ValueError
#         if stem_diameter <= 0:
#             raise ValueError
#         self.__stem_diameter = stem_diameter
#
#     @property
#     def stem_length(self):
#         return self.__stem_length
#
#     @stem_length.setter
#     def stem_length(self, stem_length):
#         if stem_length <= 0:
#             raise ValueError
#         self.__stem_length = stem_length
#
#     @property
#     def cap_diameter(self):
#         return self.__cap_diameter
#
#     @cap_diameter.setter
#     def cap_diameter(self, cap_diameter):
#         if cap_diameter <= 0:
#             raise ValueError
#         if cap_diameter <= self.__stem_diameter:
#             raise ValueError
#         self.__cap_diameter = cap_diameter
#
#     @property
#     def dim_cost(self):
#         return self.__stem_length + self.__cap_diameter
#
#     @property
#     def volume(self):
#         return math.pi * ((self.__stem_diameter/2) ** 2 * self.__stem_length + (4/6) * (self.__cap_diameter/2)**3)


# import math
#
#
# class Container:
#     ''' This is a meta class that's supposed to NOT have an initializer.
#         It's only to be extended upon.
#     '''
#     def __init__(self):
#         pass
#
#
# class Banana(Container):
#     ''' The Banana box.
#         Define the volume and dim_cost using length and radius at the widest part.
#     '''
#
#     def __init__(self, length, radius):
#         if length < 4 * radius:
#             raise ValueError
#         self.__length = length
#         self.__radius = radius
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, length):
#         if length < 4 * self.__radius:
#             raise ValueError
#         self.__length = length
#
#     @property
#     def radius(self):
#         return self.__radius
#
#     @radius.setter
#     def radius(self, radius):
#         if self.__length < 4 * radius:
#             raise ValueError
#         self.__radius = radius
#
#     @property
#     def dim_cost(self) -> float:
#         return float(self.__length + (2 * self.__radius))
#
#     @property
#     def volume(self) -> float:
#         return (4/3) * math.pi * self.__length * (self.__radius**2)
#
# try:
#     l = int(input())
#     r = int(input())
#     b = Banana(l, r)
#     print(b.length, b.radius, b.volume, b.dim_cost)
#     b.length = int(input())
#     print(b.length, b.radius, b.volume, b.dim_cost)
#     b.radius = int(input())
#     print(b.length, b.radius, b.volume, b.dim_cost)
#     print(all([x.startswith('_Banana__') for x in list(vars(b))]))
# except ValueError:
#     print("ERROR")

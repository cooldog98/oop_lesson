# import math
# class Circle:
#     def __init__(self, x, y, radius):
#         self.x = x
#         self.y = y
#         self.radius = radius
#
#     def area(self):
#         return math.pi * (self.radius**2)
#
#     def move(self, x, y):
#         self.x = x
#         self.y = y
#
#
# import math
#
# class Vector:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def length(self):
#         return math.sqrt((self.x**2) + (self.y**2))
#
#     def __str__(self):
#         return f'Vector(x={self.x}, y={self.y})'
#
#     def dot(self, v):
#         return self.x*v.x + self.y*v.y
#
#     def add(self, v):
#         return Vector(self.x+v.x, self.y+v.y)
#
#     def subtract(self, v):
#         return Vector(self.x-v.x, self.y-v.y)
#
#     def multiply(self, s):
#         return Vector(s*self.x, s*self.y)
#
# class Coin:
#     def __init__(self, value=1):
#         self.value = value
#
#     def __str__(self):
#         return f'{self.value} Baht Coin'
#
#     def get_value(self):
#         return self.value
#
#     def set_value(self, value):
#         self.value = value
#
# class Banknote:
#     def __init__(self, value=20):
#         self.value = value
#
#     def __str__(self):
#         return f'{self.value} Baht Banknote'
#
#     def get_value(self):
#         return self.value
#
#     def set_value(self, value):
#         self.value = value
#
# class Person:
#     def __init__(self, id: str = "",
#                  name="", lastname="",
#                  gender: str = "", age: int = 0):
#         self.id = id
#         self.name = name
#         self.lastname = lastname
#         self.gender = gender
#         self.age = age
#
#
#     def set_id(self, id):
#         self.id = id
#
#     def get_id(self):
#         return self.id
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_lastname(self):
#         return self.lastname
#
#     def set_lastname(self, lastname):
#         self.lastname = lastname
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, age):
#         self.age = age
#
#     def get_gender(self):
#         return self.gender
#
#     def set_gender(self, gender):
#         self.gender = gender
#
#     def __str__(self):
#         return f'{self.id}, {self.name} {self.lastname}, {self.gender}, {self.age}'
#
# class Location:
#     def __init__(self, room: str = '', floor: int = '', person: str = ''):
#         self.person = person
#         self.room = room
#         self.floor = floor
#
#     def get_person(self):
#         return self.person
#
#     def set_person(self, person):
#         self.person = person
#
#     def get_room(self):
#         return self.room
#
#     def set_room(self, room):
#         self.room = room
#
#     def get_floor(self):
#         return self.floor
#
#     def set_floor(self, floor):
#         self.floor = floor
#
#     def __str__(self):
#         if self.person == "":
#             return f'{self.room} on floor {self.floor}. No one is in this room.'
#         else:
#             return f'{self.room} on floor {self.floor}. {self.person} is in this room.'
#
# print(Location('lcu', 3,))
#
# class Radio:
#     def __init__(self, mode='FM', frequency=87.5):
#         self.mode = mode
#         self.frequency = frequency
#
#     def get_mode(self):
#         return self.mode
#
#     def set_mode(self, mode):
#         self.mode = mode
#         if mode == 'FM':
#             frequency = 87.5
#             self.frequency = frequency
#             return frequency
#         else:
#             frequency = 150
#             self.frequency = frequency
#             return frequency
#
#     def get_frequency(self):
#         return self.frequency
#
#     def set_frequency(self, frequency):
#         # in_fre = int(input())
#         if self.mode == 'FM':
#             if 87.5 <= frequency <= 108:
#                 self.frequency = frequency
#                 return self.frequency
#             else:
#                 return self.frequency
#         else:
#             if 150 <= frequency <= 280:
#                 self.frequency = frequency
#                 return self.frequency
#             else:
#                 return self.frequency
#
#     def adjust_frequency(self, frequency):
#         # x = int(input())
#         cr_frequency = self.frequency + frequency
#         if self.mode == 'FM':
#             if 87.5 <= cr_frequency <= 108:
#                 self.frequency = cr_frequency
#                 return True
#             else:
#                 return False
#
#         if self.mode == 'AM':
#             if 150 <= cr_frequency <= 280:
#                 self.frequency = cr_frequency
#                 return True
#             else:
#                 return False
#
#     def __str__(self):
#         if self.mode == 'FM':
#             return f'FM Radio: {self.frequency:.1f} MHz'
#         if self.mode == 'AM':
#             return f'AM Radio: {self.frequency:.1f} kHz'
# print(Radico('FM',87.5))
#
#
# class Car:
#     def __init__(self, gas, burning_rate):
#         self.gas = gas
#         self.burning_rate = burning_rate
#
#     def get_gas(self):
#         return self.gas
#
#     def get_burning_rate(self):
#         return self.burning_rate
#
#     def set_gas(self, gas):
#         self.gas = gas
#
#     def set_burning_rate(self, burning_rate):
#         self.burning_rate = burning_rate
#
#     def drive(self, distance):
#         gas_still = distance/self.burning_rate
#         gas_final = self.gas - gas_still
#         self.gas = gas_final
#         return self.gas
#
#     def fill_gas(self, new_gas):
#         fill_gas = new_gas + self.gas
#         self.gas = fill_gas
#         return self.gas
#
#     def __str__(self):
#         return f'Gas: {self.gas} ,Burning rate: {self.burning_rate}'
#
# print(Car(40,3))
#
# class ClassRoom:
#     def __init__(self, grade: int = 0, homeroom_teacher: str = "", student_list = [], num_student: int = 0):
#         self.grade = grade
#         self.homeroom_teacher = homeroom_teacher
#         self.student_list = student_list
#         self.num_student = num_student
#
#     def get_grade(self):
#         return self.grade
#
#     def set_grade(self, grade):
#         self.grade = grade
#
#     def get_homeroom_teacher(self):
#         return self.homeroom_teacher
#
#     def set_homeroom_teacher(self, homeroom_teacher):
#         self.homeroom_teacher = homeroom_teacher
#
#     def get_student_list(self):
#         return self.student_list
#
#     def set_student_list(self, student_list):
#         if len(self.student_list) <= 10:
#             self.student_list = student_list
#
#     def get_num_student(self):
#         return self.num_student
#
#     def set_num_student(self, num_student):
#         self.num_student = num_student
#
#     def get_student_no(self, n):
#         return self.student_list[n-1]
#
#     def add_student(self, student_name):
#         # self.num_student = len(self.student_list)
#         if self.num_student < 10:
#             self.student_list.append(student_name)
#             self.num_student += 1
#             return True
#         else:
#             return False
#
#     def change_student(self, n, new_name):
#         if self.num_student >= n > 0:
#             self.student_list[n-1] = new_name
#             return True
#         else:
#             return False
#
#     def remove_student(self, student_name):
#         # num_same_name = 0
#         for i in range(len(self.student_list)):
#             if student_name == self.student_list[i]:
#                 self.student_list.remove(student_name)
#                 num = len(self.student_list)
#                 self.num_student = num
#                 return True
#                 break
#             else:
#                 return False
#
#     def remove_student_no(self, n: int):
#         if self.num_student >= n > 0:
#             new_int = n - 1
#             self.student_list.pop(new_int)
#             # del self.student_list[new_int]
#             self.num_student -= 1
#             return True
#         else:
#             # print('mmm')
#             return False
#
#     # @property
#     # def name_student(self):
#     #     each_name = ''
#     #     for name in self.student_list:
#     #         if len(self.student_list) > 0:
#     #             each_name += f' {name}'
#     #             return each_name
#     #         elif self.student_list == []:
#     #             return each_name
#
#     def __str__(self):
#         return (f'Grade: {self.grade}\nHomeroom Teacher: {self.homeroom_teacher}\n'
#                 f'Students: {', '.join(self.student_list)}')



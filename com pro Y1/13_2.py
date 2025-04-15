# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_x(self):
#         return self.x
#
#     def set_x(self, x):
#         self.x = x
#
#     def get_y(self):
#         return self.y
#
#     def set_y(self, y):
#         self.y = y
#
#     def is_on_x_axis(self):
#         if self.y == 0:
#             return True
#         return False
#
#     def is_on_y_axis(self):
#         if self.x == 0:
#             return True
#         return False
#
#     def translate(self, distX, distY):
#         self.x += distX
#         self.y += distY
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#
# # class PointApp:
# #     p1 = Point(20, 100)
# #     p2 = Point(-40, 50)
# #     print(Point.is_on_x_axis(p1))
# #     print(Point.is_on_y_axis(p2))
# #     Point.translate(p1, -60, -50)
# #     print(p1 == p2)
# #     print(Point.__str__(p1))
# #     print(Point.__str__(p2))
# #
#
# import math
# class Line:
#     # import math
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#         self.slope = (y2 - y1) / (x2 - x1)
#         self.y_intersept = y1 - (self.slope * x1)
#
#     def contains(self, x, y):
#         if y == (self.slope*x) + self.y_intersept:
#             if min(self.x1, self.x2) <= x <= max(self.x1, self.x2):
#                 if min(self.y1, self.y2) <= y <= max(self.y1, self.y2):
#                     return True
#         return False
#
#     def get_distance(self):
#         return math.sqrt(((self.x2 - self.x1)**2) + ((self.y2 - self.y1)**2))
#
#     def get_x1(self):
#         return self.x1
#
#     def get_y1(self):
#         return self.y1
#
#     def get_x2(self):
#         return self.x2
#
#     def get_y2(self):
#         return self.y2
#
#     def get_y(self, x):
#         y = (self.slope * x) + self.y_intersept
#         if self.contains(x, y) == True:
#             return y
#         return -999.999


# class LineApp:
#     x1 = float(input('Enter x1 : '))
#     y1 = float(input('Enter y1 : '))
#     x2 = float(input('Enter x2 : '))
#     y2 = float(input('Enter y2 : '))
#     print(f'value of x1 on this line is {x1:.3f}')
#     print(f'value of x2 on this line is {x2:.3f}')
#     print(f'value of y1 on this line is {y1:.3f}')
#     print(f'value of y2 on this line is {y2:.3f}')
#     line = Line(x1, y1, x2, y2)
#     print('==========')
#     print('Check x and y are on this line ?')
#     x = float(input('Enter x : '))
#     y = float(input('Enter y : '))
#     # Line.contains(line, x, y)
#     if Line.contains(line, x, y):
#         print(f'x = {x:.3f} and y = {y:.3f} are on this line')
#     else:
#         print(f'x = {x:.3f} and y = {y:.3f} are not on this line')
#     print(f'Distance between startPoint and endPoint is {Line.get_distance(line):.3f}')
#     print('==========')
#     print('Find value of y that gives( x , y ) on this line')
#     x_another = float(input('Enter x : '))
#     y = Line.get_y(line, x_another)
#     print(f'value of y is {Line.get_y(line, x_another):.3f}')
#     if y == -999.999:
#         print(f'( x , y ) = ( {x_another:.3f} , {y:.3f} ) is not on this line')
#     else:
#         print(f'( x , y ) = ( {x_another:.3f} , {y:.3f} ) on this line')


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
#
# class CoinBankNoteApp:
#     type_coin = [Banknote(1000), Banknote(500), Banknote(100), Banknote(50), Banknote(20),
#                  Coin(10), Coin(5), Coin(2), Coin(1)]
#
#     coin = int(input('Input amount : '))
#
#     for i in type_coin:
#         still = coin//i.get_value()
#
#         if still > 0:
#             print(f'You get {still} of {i}')
#         coin -= still*i.get_value()


# class Course:
#     def __init__(self, title, course_id, credit):
#         self.title = title
#         self.course_id = course_id
#         self.credit = credit
#
#
# class Teacher:
#     def __init__(self, firstname, lastname, id):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.id = id
#
#     def __str__(self):
#         # print(f'{self.firstname} {self.lastname} ({self.id})')
#         return f'{self.firstname} {self.lastname} ({self.id})'
#
#
# class Major:
#     def __init__(self, id, name, faculty):
#         self.id = id
#         self.name = name
#         self.faculty = faculty
#
#     def __str__(self):
#         # print(f'{self.name} {self.faculty} ({self.id})')
#         return f'{self.name} {self.faculty} ({self.id})'
#
#
# class Student:
#     def __init__(self, id, firstname, lastname):
#         self.id = id
#         self.firstname = firstname
#         self.lastname = lastname
#         self.advisor = None
#         self.major = None
#         self.list_course = []
#         self.num_course = 0
#         self.total_credit = 0
#
#     def add_course(self, course):
#         if course not in self.list_course and self.total_credit + course.credit <= 25:
#             self.list_course.append(course)
#             self.num_course += 1
#             self.total_credit += course.credit
#             return True
#         return False
#
#     def drop_course(self, course):
#         if course in self.list_course:
#             self.list_course.remove(course)
#             self.num_course -= 1
#             self.total_credit -= course.credit
#             return True
#         return False
#
#     def set_advisor(self, advisor):
#         self.advisor = advisor
#
#     def set_major(self, major):
#         self.major = major
#
#     def __str__(self):
#         # print_str = ''
#         # for i in self.list_course:
#         #     print_str += f'{i} '
#         courses_str = ' '.join(course.course_id for course in self.list_course)
#         advi = str(self.advisor) if self.advisor else 'None'
#         major = str(self.major) if self.major else 'None'
#
#         return (f'Student ID: {self.id}\nName: {self.firstname} {self.lastname}\n'
#                 f'Major: {major}\nAdvisor: {advi}\nCourses: {courses_str}')
#
#
# Major('E17', 'Software & Knowledge', 'Engineering')
# print(Student(5610546231, 'Chinnaporn', 'Soonue'))

class Switch:
    def __init__(self, name, status = False):
        self.name = name
        self.status = status

    def turn(self):
        self.status = not self.status

    def clone(self):
        return Switch(f'{self.name}.copy', self.status)

    def __str__(self):
        if self.status == True:
            status_final = 'on'
            # return status_final
        else:
            status_final = 'off'
            # return status_final

        return f'switch({self.name}) is {status_final}'


class Light:
    def __init__(self, name, switch):
        self.name = name
        self.switch = switch

    def turn(self):
        self.switch.turn()

    def get_status(self):
        return self.switch.status

    def set_switch(self, new_switch):
        self.switch = new_switch

    def clone(self):
        switch_clone = self.switch.clone()
        return Light(f'{self.name}.copy', switch_clone)

    def __str__(self):
        if self.get_status() == True:
            status_final = 'on'
            # return status_final
        else:
            status_final = 'off'
        return f'light({self.name}) with switch({self.switch.name}) is {status_final}'

p1 = Switch('s1', False)
print(p1)

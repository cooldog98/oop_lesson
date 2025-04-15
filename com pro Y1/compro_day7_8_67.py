'''print('hello'+' world')

print((3*42)+(7*85))
avg = (38+12+50)/3
print(avg)

total = (10+21+32+43+54)
average = total/5
print(total)
print(average)

x,y,z = 5, 10, 15
print(x,y,z)

text1 = "I'm fine."
print(text1)

text2 = '"print" is a function'
print(text2)

text3 = '"'"That's good,"'" he said.'
print(text3)

total_seconds = 381
minutes = total_seconds//60
seconds = total_seconds % 60
print(minutes)
print(seconds)
import math'''

'''first = input('What is your first name? ')
last = input('What is your last name? ')
print("Hello,", first, last)

AD = int(input('Enter a year in A.D.: '))
BE = AD + 543
print(f'The year in B.E. is {BE}')

width = float(input("Enter rectangle's width: "))
height = float(input("Enter rectangle's height: "))
print(f'The area of the rectangle is {width*height}')'''


'''name = "Arthur"
print(f"|12345678901234567890|")
print(f"|--------------------|")
print(f'|{name:<20}|')

name = "Arthur"
print(f"|12345678901234567890|")
print(f"|--------------------|")
print(f'|{name:>20}|')

name = "Arthur"
print(f"|12345678901234567890|")
print(f"|--------------------|")
print(f'|{name:^20}|')

x = 12.3456789
print(f"|12345678901234567890|")
print(f"|--------------------|")
print(f"|{x:>20.3f}|")'''

'''Salad = 75
Soup = 85
Steak = 320
Wine = 610
Orange_Juice = 35
Pasta = 165
Friedrice = 100
total = (Salad + Soup + Steak + Wine + Orange_Juice + Pasta + Friedrice)
discounted = total*(8/100)
final = total - discounted
print(f'The discounted cost is {final:.2f}')'''

'''seconds1 = int(input('How many total seconds? '))
hours = seconds1//3600
minutes = int((seconds1%3600)//60)
seconds = seconds1 % 60
print(f'That is equal to {hours} hour(s) {minutes} minute(s) and {seconds} second(s).')'''

'''LAB = "turtlelab1.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.4",LAB)

from turtlelab1 import turtle,check
turtle.left(45)
turtle.forward(100)
turtle.left(45)
turtle.forward(50)
turtle.right(20)
turtle.forward(70)
check()'''

'''LAB = "turtlelab2.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.4",LAB)

from turtlelab2 import turtle,home,check
turtle.left(180)
turtle.forward(abs(home.x))
turtle.left(90)
turtle.forward(abs(home.y))
check()'''

'''name1 = input("Enter name #1: ")
gpa1 = float(input("Enter GPA #1: "))
name2 = input("Enter name #2: ")
gpa2 = float(input("Enter GPA #2: "))

print(f"+-----------+-------+")
print(f"|   Name    |  GPA  |")
print(f"+-----------+-------+")
print(f"| {name1:<10}| {gpa1:<6.2f}|")
print(f"| {name2:<10}| {gpa2:<6.2f}|")
print(f"+-----------+-------+")'''

'''first, last = 'Sam', 'Smith'
date, month, year = 16, 5, 2002
print(f'My name is {first}', end=' ')
print(f'{last}', )
print(f'My birthday', ':', end=' ')
print(date, month, year, sep='/')
print(f'In 2023, I a',end='')
print(f'm {2023-year} years old.',)

print()
table_num, num_guests = 7, 5
reserved_time = "11:00-13:00"
n_desserts, n_app, n_entrees = 2, 3, 5
cost = 4318.1685
print('Table #{} is reserved at {} for {} people.'.format(table_num, reserved_time, num_guests))
print('Customers pre-orders {} appetizers, {} entrees, and {} desserts.'.format(n_app, n_entrees, n_desserts))
print('After discount, the bill costs {:.2f} Baht.'.format(cost))'''

'''candies = int(input('Enter number of candies: '))
friends = int(input('Enter number of friends: '))
between = int(candies//friends)
remain = int(candies % friends)
print(f'There are {candies} candies shared between {friends} friends.')
print(f'Each friend will receive {between} candies.')
print(f'There are remaining {remain} candies that are not shared.')'''

'''width = input('What is width: ')
lenght = input('What is length: ')
sqm = (float(width)*float(lenght))//100
pounds = int(sqm)*1600
print(f'The landlord will have {int(sqm)} pieces of land available for sale.')
print(f'From the sale, he can earn {pounds} pounds.')'''

'''base = float(input('What is base: '))
height = float(input('What is height: '))
area = (base*height)/2
print(f'For triangle with base={base:.3f} and height={height:.3f}, area is {area:.3f}.')'''

'''x = float(input('What is x: '))
y = float(input('What is y: '))
result = (((x-y)*3.14)/((x+y)*(0.15+(y/x))))
print(f'The result value is {result:.5f}')'''

'''name = input('What is your name: ')
birthyear = int(input('What is your birthyear: '))
currentyear = int(input('What is current year: '))
old = currentyear - birthyear
print(f'Welcome, {name.capitalize()}')
print(f'Currently, you are {old} years old.')'''

'''LAB = "turtlelab2x.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab2x import turtle,home,shop,check
turtle.left(90)
turtle.forward(abs(shop.y))
turtle.right(90)
turtle.forward(abs(shop.x))

turtle.forward(abs(shop.x - home.x))
turtle.left(90)
turtle.forward(abs(shop.y - home.y))
check()'''

'''import math
x,y,z = 8,4,3
distance = math.sqrt(math.pow(x,2)+math.pow(y,2)+math.pow(z,2))
print(distance)'''

'''def song(animal,sound):
    print(f"Old MACDONALD had a farm E-I-E-I-O")
    print(f"And on his farm he had a {animal} E-I-E-I-O")
    print(f"With a {sound} {sound} here")
    print(f"And a {sound} {sound} there")
    print(f"Here a {sound}, there a {sound}")
    print(f"Everywhere a {sound} {sound}")

def rectangle_area(length,width):
    area = length*width
    return area'''

'''def compute_double(value):
    return value*2

def print_double(value):
    print(value*2)'''


'''def compute_circle_area(r):
    areadef = math.pi*r**2
    return areadef

def compute_circle_circumference(r):
    circumferencedef = 2*math.pi*r
    return circumferencedef

import math
radius = float(input('Enter circle radius: '))
area = compute_circle_area(radius)
circumference = compute_circle_circumference(radius)
print(f'Area of circle is {area:.2f}.')
print(f'The circumference of the circle is {circumference:.2f}.')'''


'''def compute_circle_area(radius):
    areacircledef = math.pi*radius**2
    return areacircledef
def compute_rectangle_area(width,length):
    arearectangledef = width*length
    return arearectangledef

import math
width1 = float(input('Please enter width: '))
length1 = float(input('Please enter length: '))
diameter = float(input('Please enter diameter: '))
radius1 = diameter/2
areacircle = compute_circle_area(radius1)
arearectangle = compute_rectangle_area(width1, length1)
lawn = arearectangle - areacircle
print(f'The area of the lawn is {lawn:.2f} sq.m.')'''

# run in shell mode in pycharm error but in elab can?


# def round_to_full_hour(minutes):
#     hours = math.ceil(minutes/60)
#     return hours
#
# def get_parking_payment(hours, rate):
#     pay = hours*rate
#     return pay
#
# import math
# minutes1 = float(input('Enter parking duration in minutes: '))
# rate = 25
# hours2 = round_to_full_hour(minutes1)
# payment = get_parking_payment(hours2, rate)
# total = math.ceil(hours2)*rate
# print(f'The parking fee rate is 25 Baht/hour.')
# print(f'Your parking payment is {total:.0f} Baht for {minutes1:.0f} minutes.')

#shell mode can't work

'''def compute_total_savings(principal, interest_rate, number_of_years):
    savings = principal * ((1 + (interest_rate/100)) ** number_of_years)
    return savings

principal = float(input('Input principal: '))
interest_rate = float(input('Input interest rate: '))
number_of_years = int(input('Input number of years: '))
total_savings = compute_total_savings(principal, interest_rate, number_of_years)
print(f'Total savings amount after {number_of_years} years is {total_savings:.2f} Baht.')'''

'''def change_log_base(x,a,b):
    import math
    log = ((math.log(x,b))/math.log(a,b))
    return math.log(x,a)

import math
x = float(input('Input x: '))
a = float(input('Input a: '))
b = float(input('Input b: '))
log1 = math.log(x,a)
log2 = change_log_base(x,a,b)
print(f'Logarithm of {x:.3f} with base {a:.3f} = {log1:.3f}')
print(f'Logarithm of {x:.3f} with base {b:.3f} / Logarithm of {a:.3f} with base {b:.3f} = {log2:.3f}')'''

'''def print_dash_dash():
    print(" ##  ## ")

def print_dash():
    print("   ##   ")

def print_line():
    print(" ###### ")

def print_H():
    print_dash_dash()
    print_dash_dash()
    print_line()
    print_line()
    print_dash_dash()
    print_dash_dash()


def print_I():
    print_line()
    print_line()
    print_dash()
    print_dash()
    print_line()
    print_line()


def print_O():
    print_line()
    print_line()
    print_dash_dash()
    print_dash_dash()
    print_line()
    print_line()

print_H()
print()
print_I()
print()
print_H()
print()
print_O()'''

'''def compute_rectangle_area(first_side, second_side):
    area = first_side*second_side
    return area

def compute_surface_area(width,length,height):
    areacuboid = (2*compute_rectangle_area(width, length))+(2*compute_rectangle_area(width, height))+(2*compute_rectangle_area(length, height))
    return areacuboid

def compute_volume(width,length,height):
    volume = width*length*height
    return volume

width1 = float(input('Enter width: '))
length1 = float(input('Enter length: '))
height1 = float(input('Enter height: '))
print(f'For [{width1:.2f} x {length1:.2f} x {height1:.2f}] cuboid:')
surface_area = compute_surface_area(width1, length1, height1)
volume = compute_volume(width1, length1, height1)
print(f'Surface area = {surface_area:.3f}')
print(f'Volume = {volume:.3f}')
print()
width2 = 2*width1
length2 = 2*length1
height2 = 2*height1
print('After doubling each side, ')
print(f'For [{width2:.2f} x {length2:.2f} x {height2:.2f}] cuboid:')
surface_area2 = compute_surface_area(width2, length2, height2)
volume2 = compute_volume(width2, length2, height2)
print(f'Surface area = {surface_area2:.3f}')
print(f'Volume = {volume2:.3f}')'''

# def compute_rectangle_area(first_side, second_side):
#     area = first_side*second_side
#     return area
#
# for _ in range(4):
#     width = float(input("Enter width: "))
#     length = float(input("Enter length: "))
#     area = compute_rectangle_area(width, length)
#     print(f"Rectangle area = {area:.3f}")


'''def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    return first / second

def calculate(first, second, operand):
    result = 0
    if operand == '+':
        result = add(first, second)
    elif operand == '-':
        result = subtract(first, second)
    elif operand == '*':
        result = multiply(first, second)
    elif operand == '/':
        result = divide(first, second)
    return result

firstnumber = float(input('Input the first number: '))
secondnumber = float(input('Input the second number: '))
operand = input('Input the operator: ')
result = calculate(firstnumber, secondnumber, operand)
print(f'{firstnumber:.2f} {operand} {secondnumber:.2f} = {result:.2f}')'''

'''LAB = "turtlelab3.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.0",LAB)

from turtlelab3 import turtle,home,check
from math import degrees,atan
distance = (home.x**2 + home.y**2)**0.5
angle = 180 - degrees(atan(abs(home.y/home.x)))
turtle.left(angle)
turtle.forward(distance)
check()'''

# LAB = "turtlelab3x.py"
# import urllib.request
# urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)
#
# from turtlelab3x import turtle,home,shop,check
# from math import degrees,atan
# distance = (shop.x**2 + shop.y**2)**0.5
# angle = degrees(atan(abs(shop.y/shop.x)))
# turtle.left(angle)
# turtle.forward(distance)
# distance2 = (home.x**2 + home.y**2)**0.5
# angle2 = degrees(atan(abs(home.y/home.x)))
# turtle.left(angle2 - angle)
# turtle.forward(distance2 - distance)
# check()

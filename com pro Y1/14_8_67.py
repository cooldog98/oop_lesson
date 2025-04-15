'''def myfunc():
    y = 88
    print(f"Inside of myfunc(), x={x}, y={y}")
x = 11
y = 22
print(f"Outside of myfunc(), x={x}, y={y}")
myfunc()

x = 33
y = 44
print(f"Outside of myfunc(), x={x}, y={y}")
myfunc()'''

'''def usd_to_thb(usd):
    thai = EXCHANGE_RATE*100
    return thai

EXCHANGE_RATE = 34.09
print(f"The current exchange rate is {EXCHANGE_RATE} THB per USD")
print(f"You get {usd_to_thb(100):.2f} Thai Baht for 100 USD")

EXCHANGE_RATE = 33.15
print(f"The current exchange rate is {EXCHANGE_RATE} THB per USD")
print(f"You get {usd_to_thb(100):.2f} Thai Baht for 100 USD")

EXCHANGE_RATE = 35.26
print(f"The current exchange rate is {EXCHANGE_RATE} THB per USD")
print(f"You get {usd_to_thb(100):.2f} Thai Baht for 100 USD")'''

'''def read_triangle_inputs():
    base = float(input('Enter triangle base: '))
    height = float(input('Enter triangle height: '))
    return base, height

def compute_triangle_area():
    area = (base * height)/2
    return area

base, height = read_triangle_inputs()
area = compute_triangle_area()
print(f"Triangle\'s area = {area:.3f}")'''

# def get_bmi(weight,height):
#     return weight/(height**2)
#
# def calculate_distance(v, a, t):
#     return v*t + 0.5 * a * t **2

# def compute_work(force,dist=1,angle=0):
#     from math import cos, radians
#     return force * dist * cos(radians(angle))

# def read_weight_height():
#     weight = float(input('Enter your weight (in kg): '))
#     height = float(input('Enter your height (in cm): '))
#     return weight, height
# def get_bmi(weight,height):
#     bmi = weight / ((height*0.01) ** 2)
#     return bmi
#
# weight,height = read_weight_height()
# bmi = get_bmi(weight = weight,height = height)
# print(f'Your Body Mass Index (BMI) is {bmi:.2f}')

# def read_trapezoid():
#     print('Specify your trapezoid\'s properties.')
#     sidea = float(input('What is the length of side a: '))
#     sideb = float(input('What is the length of side b: '))
#     hight = float(input('What is the height? '))
#     return sidea, sideb, hight
#
# def trapezoid_area(sidea, sideb, hight):
#     area = ((sidea+sideb)/2)*hight
#     return area
#
# side1,side2,height = read_trapezoid()
# area = trapezoid_area(sidea=side1, sideb=side2, hight=height)
# print(f'The area of the trapezoid is {area:.2f}')

# KILOMETERS_PER_MILE = 1.609
# def convert_miles_to_kms(m):
#     kilometer = m * KILOMETERS_PER_MILE
#     return kilometer
#
# miles = float(input('Please input distance in miles: '))
# kilometers = convert_miles_to_kms(miles)
# print(f'After conversion, the distance is {kilometers:.2f} kilometers.')

'''FIVEHUNDRED = 500
HUNDRED = 100
TWENTY = 20


def read_all_inputs():
    name = input('Please input your name: ')
    charge = float(input('Please input your charge: '))
    payment = float(input('Please input your payment: '))
    return name,charge,payment


def calculate_change(charge, payment):
    finalcharge = payment-charge
    return finalcharge


def find_change_in_bills(charge):
    import math
    fivehundredbills = (charge//FIVEHUNDRED)
    hundredbills = ((charge - FIVEHUNDRED*fivehundredbills) // HUNDRED)
    twentybills = ((charge - FIVEHUNDRED*fivehundredbills - HUNDRED*hundredbills) // TWENTY)
    coins = (charge - FIVEHUNDRED*fivehundredbills - HUNDRED*hundredbills - TWENTY*twentybills)
    fivehundredbills = int(fivehundredbills)
    hundredbills = int(hundredbills)
    twentybills = int(twentybills)
    return fivehundredbills, hundredbills, twentybills, coins


def show_change(_name, _charge1, _fivezerozero_baht_bills, _onezerozero_baht_bills, _twozero_baht_bills, _coins):
    line1 = (f'Hello, {_name}.  Thank you for visiting.')
    line2 = (f'As for change, you receive {_charge1:.2f} Baht.')
    line3 = (f'You receive {_fivezerozero_baht_bills} 500-Baht bills, {_onezerozero_baht_bills} 100-Baht bills, '
             f'{_twozero_baht_bills} 20-Baht bills, and {_coins:.2f} Baht change in coins.')
    print(line1)
    print(line2)
    print(line3)


_name, _charge, payment = read_all_inputs()
_charge1 = calculate_change(_charge, payment)
_fivezerozero_baht_bills, _onezerozero_baht_bills, _twozero_baht_bills, _coins = find_change_in_bills(_charge1)
show_change(_name, _charge1, _fivezerozero_baht_bills, _onezerozero_baht_bills, _twozero_baht_bills, _coins)'''


'''def read_one_input(text):
    cylinder = float(input(f'Please input {text} of cylinder: '))
    return cylinder


def get_volume(height, radius=1):
    import math
    volume = math.pi * (radius ** 2) * height
    return volume


def get_surface_area(height, radius=1):
    import math
    surface = (2*math.pi*radius*height)+(2*math.pi*(radius**2))
    return surface


def display(text, value):
    print(f'The {text} of cylinder is {value:.3f}')


import math
radius = read_one_input('radius')
height = read_one_input('height')
vol = get_volume(height, radius)
area = get_surface_area(height, radius)
display("volume", vol)
display("surface area", area)'''


'''def read_one_input(text):
    length = float(input(f'Please input length of {text}: '))
    return length


def read_multiple_inputs():
    side1 = read_one_input('side1')
    side2 = read_one_input('side2')
    side3 = read_one_input('side3')
    return side1, side2, side3


def calculate_tri_perimeter(side1, side2, side3):
    perimeter = side1 + side2 + side3
    return perimeter


def calculate_tri_area(perimeter, side1, side2, side3):
    import math
    s = perimeter/2
    area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
    return area


def display_all_outputs(shape, find1, ans1, find2, ans2):
    print(f'The {find1} of {shape} is {ans1:.2f}')
    print(f'The {find2} of {shape} is {ans2:.2f}')

import math
a,b,c = read_multiple_inputs()
s = calculate_tri_perimeter(a,b,c)
area = calculate_tri_area(s,a,b,c)
display_all_outputs("triangle", "perimeter", s, "area", area)'''


'''TV_PRICE = 7200
AUDIO_PRICE = 3600


def read_amount():
    tv = int(input('How many TVs do you want? '))
    audio = int(input('How many audio systems do you want? '))
    return tv, audio


def compute_total(tvs=0, audio=0):
    total = (tvs*TV_PRICE) + (audio*AUDIO_PRICE)
    return total


def get_output_str(total=0):
    return f'Your total amount is {total:.2f} Baht.'

tv, audio = read_amount()
total = compute_total(tv, audio)
output_str = get_output_str(total)
print(output_str)'''


'''def read_vector(text):
    print(f'{text}')
    x = float(input('Input value of x: '))
    y = float(input('Input value of y: '))
    return x, y


# def dot_product(ax, ay, bx, by):
#     result = (ax*bx)+(ay*by)
#     return result


def convert_vector_to_str(x, y):
    return f'[{x:.2f}, {y:.2f}]'


# ax, ay = read_vector('For vector A')
# bx, by = read_vector('For vector B')
# result1 = dot_product(ax, ay, bx, by)
# first = convert_vector_to_str(ax, ay)
# second = convert_vector_to_str(bx, by)
# print(f'Dot product of {first} and {second} is {result1:.2f}')


def add(ax, ay, bx, by):
    return ax + bx, ay + by


def subtract(ax, ay, bx, by):
    return ax - bx, ay - by


def calculate(ax,ay,bx,by,choice="+"):
    if choice == "+":
       cx,cy = add(ax,ay,bx,by)          # Call function add
    elif choice == "-":
       cx,cy = subtract(ax,ay,bx,by)     # Call function subtract
    return cx, cy

ax, ay = read_vector('For vector A')
bx, by = read_vector('For vector B')
choice = input('What to do with vectors? ')
cx, cy = calculate(ax, ay, bx, by, choice)
result = convert_vector_to_str(cx, cy)
first = convert_vector_to_str(ax, ay)
second = convert_vector_to_str(bx, by)
print('{} {} {} = {}'.format(first, choice, second, result))'''


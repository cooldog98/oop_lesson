'''def is_triangle(onest, twond, threerd):
    if onest + twond > threerd:
        if onest + threerd > twond:
            if twond + threerd > onest:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def read_nonnegative(text):
    from sys import exit
    number = float(input(f'{text}'))
    if number >= 0:
        return number
    else:
        print('Invalid value: input must be nonnegative')
        exit()


first = read_nonnegative("Enter 1st line's length: ")
second = read_nonnegative("Enter 2nd line's length: ")
third = read_nonnegative("Enter 3rd line's length: ")
is_triangle(onest=first, twond=second, threerd=third)
if is_triangle(onest=first, twond=second, threerd=third) == True:
    print("It's a triangle.")
else:
    print("It's not a triangle.")'''


'''def real_valued():
    x = float(input('Enter x: '))
    y = float(input('Enter y: '))
    if 5<x<=20:
        result = (4*x*y)+5
        print(f"f({x:.3f},{y:.3f}) = {result:.3f}")
    else:
        result2 = x**2 - 100*y
        return print(f"f({x:.3f},{y:.3f}) = {result2:.3f}")

real_valued()'''


def min_of_three(a, b, c):
    if a < 0 or b < 0 or c < 0:
        if a < (b and c):
            return a
        elif b < (a and c):
            return b
        elif c < (a and b):
            return c
    elif a < 0 and b < 0 and c < 0:
        an = a*(-1)
        bn = b*(-1)
        cc = c*(-1)
        if an > (bn and cc):
            return an
        elif bn > (a and cc):
            return bn
        elif cc < (a and b):
            return cc
    else:
        if a < (b and c):
            return a
        elif b < (a and c):
            return b
        elif c < (a and b):
            return c
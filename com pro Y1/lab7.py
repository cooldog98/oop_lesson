'''def letter_grade(score):
    if score < 50:
        return "F"
    elif 50 <= score < 60:
        return "D"
    elif 60 <= score < 70:
        return "C"
    elif 70 <= score < 80:
        return "B"
    else:
        return "A" '''


'''def bmi():
    weight = int(input('Please enter your weight in kg: '))
    height = int(input('Please enter your height in cm: '))
    meter = height * 0.01
    bmi = weight / meter**2
    return bmi


def interpretation(BMI):
    if BMI < 18.5:
        print("You are underweight")
    elif 18.5 <= BMI < 25:
        print("You are normal")
    elif 25 <= BMI < 30:
        print('You are overweight')
    else:
        print('You are obese')


BMI = bmi()
print(f'Your BMI: {BMI:.2f}')
interpretation(BMI)'''


'''def score():
    homework = int(input('What is the homework percentage? '))
    midterm = int(input('What is the midterm percentage? '))
    final = int(input('What is the final percentage? '))
    homework1 = homework * 0.05
    midterm1 = midterm * 0.35
    final1 = final * 0.60
    total = homework1 + midterm1 + final1
    print(f'Total score: {total:.2f}')
    return total


def range(total):
    if total >= 80:
        print('Your grade is A')
    elif 75 <= total < 80:
        print('Your grade is B+')
    elif 70 <= total < 75:
        print('Your grade is B')
    elif 65 <= total < 70:
        print('Your grade is C+')
    elif 60 <= total < 65:
        print('Your grade is C')
    elif 55 <= total < 60:
        print('Your grade is D+')
    elif 50 <= total < 55:
        print('Your grade is D')
    else:
        print('Your grade is F')

total = score()
range(total)'''


'''def leap_year(year):
    if year <= 0:
        print('Invalid input: the year must be positive')
    elif 1 <= year <= 1751:
        if year % 4 == 0:
            print(f'The year {year} (AD) is a leap year')
        else:
            print(f'The year {year} (AD) is not a leap year')
    elif year > 1751:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f'The year {year} (AD) is a leap year')
        else:
            print(f'The year {year} (AD) is not a leap year')


year = int(input('What is the year in AD? '))
leap_year(year)'''


'''def function(x):
    if x <= 15:
        formula = (2*x)+10
        print(f'f({x:.3f}) = {formula:.3f}')
    elif 15 < x <= 35:
        formula2 = 3*(x**2)
        print(f'f({x:.3f}) = {formula2:.3f}')
    else:
        formula3 = 2*(x**3)-5
        print(f'f({x:.3f}) = {formula3:.3f}')


x = float(input('Enter a real number: '))
function(x)'''


'''def location(x, y):
    if x == 0 and y != 0:
        print(f'The point ({x:.2f},{y:.2f}) is on the y-axis.')
    elif y == 0 and x != 0:
        print(f'The point ({x:.2f},{y:.2f}) is on the x-axis.')
    elif x == 0 and y == 0:
        print(f'The point ({x:.2f},{y:.2f}) is at the origin.')
    else:
        if x > 0 and y > 0:
            print(f'The point ({x:.2f},{y:.2f}) is in quadrant 1.')
        elif x < 0 and y > 0:
            print(f'The point ({x:.2f},{y:.2f}) is in quadrant 2.')
        elif x < 0 and y < 0:
            print(f'The point ({x:.2f},{y:.2f}) is in quadrant 3.')
        elif x > 0 and y < 0:
            print(f'The point ({x:.2f},{y:.2f}) is in quadrant 4.')


print('Input a point (x,y): ')
x = float(input('x = ? '))
y = float(input('y = ? '))
location(x, y)'''


'''def triangle(first, second, third):
    if first**2 == (second**2 + third**2) or second**2 == (first**2 + third**2) or third**2 == (first**2 + second**2):
        print("It's a right triangle.")
    elif first + second > third and second + third > first and third + first > second:
        print("It's a triangle but not a right triangle.")
    else:
        print("It's not a triangle.")


first = float(input("Enter 1st line's length: "))
second = float(input("Enter 2nd line's length: "))
third = float(input("Enter 3rd line's length: "))
triangle(first, second, third)'''




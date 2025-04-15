'''i = 10
while i < 22:
    print(i)
    i += 3
print()
for i in range(10,22,3):
    print(i)'''


'''for i in range(0,-10,-2):
    print(i)
print()
i = 0
while i > -10:
    print(i)
    i += -2'''

'''i = 10
while i < 12:
    print(f'{i:.2f}')
    i += 0.15'''


'''total = 0
number = float(input("Enter a number (-1 to stop): "))
while number != -1:
    total = total + number
    number = float(input("Enter a number (-1 to stop): "))
print(f"Total is {total}")
print()'''

'''PASSWORD = "I love Python"
s = input("Enter password: ")
while s != PASSWORD:
    print("Incorrect password.  Access denied.")
    s = input("Enter password: ")
print("Correct password.  Access granted.")'''


'''sum = 0
i = 1
while i <= 100:
    sum = sum + i
    print(i, sum)
print(f"The sum is {sum}")'''

'''positive = []
negative = []
ans = 0
numbers = float(input("Enter a number (to exit, just enter zero): "))
while numbers != 0:
    ans = ans + numbers
    if numbers < 0:
        negative.append(numbers)
    elif numbers >= 1:
        positive.append(numbers)
    numbers = float(input("Enter a number (to exit, just enter zero): "))
print(f'The sum of all positive numbers is {sum(positive):.2f}')
print(f'The sum of all negative numbers is {sum(negative):.2f}')'''


'''def fah_to_cel(start, end, step): # version 2
    print(f"{'Fahrenheit':>12}{'Celcius':>12}")
    print(f"{'----------':>12}{'-------':>12}")
    fah = start
    while (fah < end) and (step > 0):
        cel = (5/9)*(fah-32)
        print(f"{fah:12.2f}{cel:12.2f}")
        fah = fah + step
    while (fah > end) and (step < 0):
        cel = (5/9)*(fah-32)
        print(f"{fah:12.2f}{cel:12.2f}")
        fah = fah + step
    print(f"{'----------':>12}{'-------':>12}")'''

'''all_num = []
num = '0'

num_input = input("Enter a number (just [Enter] to exit): ")
if num_input == '':
    print('Nothing to do.')
elif num_input != '':
    all_num.append(float(num_input))
    while num_input != '':
        num += num_input
        num_input = (input("Enter a number (just [Enter] to exit): "))
        if not num_input:
            break
        all_num.append(float(num_input))

    ma = float(max(all_num))
    mi = float(min(all_num))
    SUM = [float(num) for num in all_num]
    ave = (sum(SUM))/len(all_num)
    print(f'The maximum is {ma:.2f}')
    print(f'The minimum is {mi:.2f}')
    print(f'The average is {ave:.2f}')'''


'''h = float(input("What is the well's depth? "))
u = float(input('How high the frog can jump up? '))
d = float(input('How far the frog slips down? '))
if h == u and h == d:
    print(f'The frog is free on day 1.')
    exit()
elif u == d or u < d:
    print('The frog will never escape from the well.')
    exit()
frog_depth = h
day = 0
while frog_depth > 0:
    day = day + 1
    frog_depth = frog_depth - u
    frog_depth1 = frog_depth + d
    print(f'On day {day} the frog leaps to the depth of {frog_depth:.0f} meters.')
    print(f'At night he slips down to the depth of {frog_depth1:.0f} meters.')
    if frog_depth1 < u:
        break
    frog_depth = frog_depth1
    while frog_depth > 0:
        day = day + 1
        frog_depth = frog_depth - u
        frog_depth1 = frog_depth + d
        print(f'On day {day} the frog leaps to the depth of {frog_depth:.0f} meters.')
        print(f'At night he slips down to the depth of {frog_depth1:.0f} meters.')
        frog_depth = frog_depth1 - u

day = day + 1
print(f'The frog is free on day {day}.')'''





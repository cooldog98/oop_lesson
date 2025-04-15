'''PASSWORD = "I love Python"

while True:
    s = input("Enter password: ")
    if s == PASSWORD:
        break
    print("Incorrect password.  Access denied.")

print("Correct password.  Access granted.")'''


# n = 1001
#
# while True:
#     n = 3003
#     if n % 33 == 0 and n % 273 == 0:
#         break
# print(f"The value of n is {n}")


'''for i in range(5,10):
    print(f"i = {i}")
    for j in range(1,3):
        print(f"  j = {j}")'''


'''for i in range(1,6):
    print(f"i = {i}")
    for j in range(i,0,-1):
        print(f"  j = {j}")'''

'''for i in range(3):
    for j in range(1,5):
        nspaces = 4 - j
        nstars = (j*2) - 1
        print((' ' * nspaces) + ('*' * nstars))'''


'''def f(n):
    sum = 0
    for i in range(n + 1):
        for j in range(n + 1):
            print(f'j{i} = {j}')
            sum = sum + i
    return sum'''


'''n = input('Enter N (or just ENTER to quit): ')
i = 0
while n != '':
    for i in range(1,13):
        n = int(n)
        aws = n * i
        print(f'{n} x {i} = {aws}')
    n = input('Enter N (or just ENTER to quit): ')'''



'''password = 'I love Python'
enter = input('Enter password please: ')
for i in range(3):
    while enter != password:
        i = i + 1
        print(f'Incorrect password, attempt #{i}')
        print('Access not allowed')
        enter = input('Enter password please: ')
        if i == 2:
            print(f'Incorrect password, attempt #{i+1}')
            print('Access not allowed')
            print('Maximum attempts exceeded')
            exit()
print('Correct password')
print('Access granted')'''


'''bushes = int(input('How many bushes? '))
size = int(input('What is the bush size? '))
for i in range(bushes):
    for j in range(1,size+1):
        sp = size - j
        j = ((j*2) - 1)
        print((' ' * sp) + ('*' * j))'''

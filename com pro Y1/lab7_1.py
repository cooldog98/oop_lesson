'''msg = input("What do you want me to say? ")
num = int(input("How many times you want me to say it? "))
for i in range(num):
    print(msg+' #'+str(i+1))'''


'''def g(x):
    return x**2

print(" x | g(x)")
print("---+---------------------------------")
for x in range(5):
    bars = "#" * round(g(x+1))
    print(f" {x+1} | {bars} ({g(x+1)})")'''


'''for i in range(30,20,-2):
    print(f"i = {i}")'''


'''import math

def f(n):
    return 15 + 10*math.sin(n/10)

print("  n | f(n)")
print("----+-------------------------------------------------")
for n in list(range(0,100,5)):
    spaces = " " * round(f(n))
    print(f" {n:2} | {spaces}*")'''



'''msg = input("Enter a message: ")
for i in range(len(msg)):
    print(f"Character {i+1} is {msg[i]}")'''

'''msg = input("Enter a message: ")

out = ""
for i in range(0,len(msg),2):
    out = out+msg[i]
print(out)

out = ""
for i in range(1,len(msg),2):
    out = out+msg[i]
print(out)'''


'''size = int(input('What is the size of block? '))
character = input('Enter the character to use: ')


for i in range(size):
    print(character*size)'''


string = input('What is your message? ')
k = -1
spaces = " "


for i in string:
    k = k+1
    print(f'{spaces*k}{i}')


'''seq = [1,4,9,16,25,36,49]
for i in range(len(seq)):
    print(f"The member at index {i} is {seq[i]}")'''


'''seq = [2,3,5,7,11,13,17,19]
for i in range(0,len(seq)-2):
    print(seq[i])
    print(len(seq))'''


'''hours = int(input('Enter numbers of hours: '))

for i in range(hours):
    hours1 = i + 1
    produces = 180 * hours1
    profit = 72 * hours1
    print(f'In {hours1} hour(s), my factory produces {produces} candies, and I make profit of {profit:.2f} Baht.')'''


# lab5_2 ex3
'''def min_of_three(a,b,c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    elif c <= a and c <= b:
        return c'''


seq = [1,2,3,4,5,6,7]
for i in range(0,5,(len(seq)-len(seq)+1)):
    print(seq[i])

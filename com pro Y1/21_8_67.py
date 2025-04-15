'''def parking_fee(hours):
    fee = hours*20
    if hours >= 24:
        extra = fee + 100
        return extra
    return fee'''

'''def calling_charge(duration):
    if duration >= 30:
        rate = 1
    else :
        rate = 2
    return duration*rate'''


'''def number():
    tv = int(input('Number of TVs: '))
    dvd = int(input('Number of DVD players: '))
    audio = int(input('Number of audio systems: '))
    paymenttv = 6000*tv
    paymentdvd = 1500*dvd
    paymentaudio = 3000*audio
    return paymenttv, paymentdvd, paymentaudio


def discount():
    if total >= 20000:
        discount1 = total*0.1
        pay = total - discount1
        print(f'You got a discount of {discount1:.2f} baht.')
        print(f'Your payment is {pay:.2f} baht. Thank you.')
    else:
        print(f'Your payment is {total:.2f} baht. Thank you.')


paymenttv, paymentdvd, paymentaudio = number()
total = paymenttv + paymentdvd + paymentaudio
print(f'The total amount is {total:.2f} baht.')
discount()'''


'''def coefficient():
    from sys import exit
    first = float(input('1st coefficient: '))
    if first == 0.0:
        print("1st coefficient can't be zero. Program exits.")
        exit()
    else:
        second = float(input('2nd coefficient: '))
        third = float(input('3rd coefficient: '))

        return first, second, third


def discriminant(first, second, third):
    import math
    value = ((second) ** 2 - (4 * first * third))
    if value > 0:
        ans1 = ((-second)+math.sqrt(value))/(2*first)
        ans2 = ((-second)-math.sqrt(value))/(2*first)
        print(f'Two real roots: {ans1:.3f} and {ans2:.3f}')
    elif value == 0:
        ans = (-second)/(2*first)
        print(f'One real root: {ans:.3f}')  
    else:
        ans1_ = ((-second)/(2*first))
        ans2_ = ((math.sqrt((-1)*value))/(2*first))
        if ans2_ < 0:
            ans2_new = ans2_*(-1)
            print(f'Two complex roots: {ans1_:.3f}+{ans2_new:.3f}i and {ans1_:.3f}-{ans2_new:.3f}i')
        else:
            print(f'Two complex roots: {ans1_:.3f}+{ans2_:.3f}i and {ans1_:.3f}-{ans2_:.3f}i')


first, second, third = coefficient()
discriminant(first, second, third)'''


LAB = "turtlelab5.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.1",LAB)

from turtlelab5 import turtle,donnie,check
turtle.left(donnie.x)
turtle.forward(donnie.y)
check()
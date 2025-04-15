#import turtle

#turtle.shape("turtle")
#turtle.left(90)
#turtle.forward(70)
#turtle.right(90)
#turtle.forward(70)
#turtle.left(90)
#turtle.forward(70)

'''celsius_str = input('Enter temp in degrees Celsius: ')
celsius = float(celsius_str)

# Fill in the code below
fahrenheit = float((9 * celsius) + float(160))/float(5)
romer = (float(9) * celsius)/float(5)
kelvin = celsius + float(273.15)

# Print the result
print('Degrees Fahrenheit is ' + str(fahrenheit))
print('Degrees Romer is ' + str(romer))
print('Degrees Kelvin is ' + str(kelvin))'''

import turtle


# Write entire function on your own.
#def draw_spike(length):


# draw your spike. Not that hard?

# Replace the ???s
#length = 100
def draw_spike_row():
    length = 100
    while turtle.forward(150):  # specify when to keep continue drawing
        draw_spike_row()  # call the draw_spike function
        print(length - 1)  # reduce the length
        turtle.left(90)
        turtle.forward(length)
        print(length - 1)


    # DO NOT MODIFY BELOW THIS LINE
turtle.color("black")
turtle.seth(180)
turtle.pu()
turtle.forward(150)
turtle.seth(0)
turtle.pd()
draw_spike_row()
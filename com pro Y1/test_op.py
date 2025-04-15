import turtle
import random
choice = int(input('Which art do you want to generate?\nEnter a number between 1 to 9 inclusive: '))
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)


class Turtle:
    def __init__(self, choice):
        self.choice = choice
        self.num_side = self._num_side()
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.border_size = random.randint(1, 10)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.reduction_ratio = 0.618

    # @property
    # def choice(self):
    #     return self.choice

    # @choice.setter
    def _num_side(self):
        if self.choice == 1:
            num_side = choice + 2
            self.choice = num_side
            return self.choice

        elif self.choice == 2:
            num_side = choice + 2
            self.choice = num_side
            return self.choice

        elif self.choice == 3:
            num_side = choice + 2
            self.choice = num_side
            return self.choice

        elif self.choice == 4:
            num_side = random.randint(3, 5)
            self.choice = num_side
            return self.choice

        elif self.choice == 8:
            num_side = random.randint(3, 5)
            self.choice = num_side
            return self.choice

        elif self.choice == 9:
            num_side = random.randint(3, 5)
            self.choice = num_side
            return self.choice

        else:
            num_side = choice - 2
            self.choice = num_side
            return self.choice

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_side):
            turtle.forward(self.size)
            turtle.left(360 / self.num_side)
        turtle.penup()

    def choice_five(self):
        self.size *= self.reduction_ratio
        turtle.penup()
        turtle.forward((self.size * self.reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward((self.size * self.reduction_ratio) / 2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]

    def choice_n(self):
        self.size *= self.reduction_ratio
        turtle.penup()
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]

    def draw(self, iterat=3):
        for i in range(iterat):
            self.draw_polygon()
            if choice == 9:
                self.choice_n()
            elif 5 <= choice <= 8:
                self.choice_five()


for _ in range(20):
    drawing = Turtle(choice)
    drawing.draw()

turtle.done()

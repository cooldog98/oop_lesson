# LAB = "turtlelab4.py"
# import urllib.request
# urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.3",LAB)
#
# from turtlelab4 import turtle,check
#
# def create_square(size):
#     """Commands the Turtle to create a square of the size specified"""
#     turtle.forward(size)
#     turtle.left(90)
#     turtle.forward(size)
#     turtle.left(90)
#     turtle.forward(size)
#     turtle.left(90)
#     turtle.forward(size)
#     turtle.left(90)
#
#
# def create_triangle(size):
#     """Commands the Turtle to create a triangle of the size specified"""
#     turtle.forward(size)
#     turtle.left(120)
#     turtle.forward(size)
#     turtle.left(120)
#     turtle.forward(size)
#     turtle.left(120)
#
# check()

# LAB = "turtlelab5.py"
# import urllib.request
# urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.1",LAB)
#
# from turtlelab5 import turtle,donnie,check
# from math import degrees,atan
# # turtle.left(90)
# if donnie.x > 0:
#     # distance = (donnie.x ** 2 + donnie.y ** 2) ** 0.5
#     # angle = degrees((abs(donnie.y / donnie.x)))
#     turtle.forward(donnie.x)
#     if donnie.y > 0:
#         turtle.left(90)
#         turtle.forward(donnie.y)
#     else:
#         turtle.right(90)
#         turtle.backward(donnie.y)
#     check()
# elif donnie.x < 0:
#     # distance = (donnie.x ** 2 + donnie.y ** 2) ** 0.5
#     # angle = degrees((abs(donnie.y / donnie.x)))
#     turtle.backward(donnie.x)
#     if donnie.y > 0:
#         turtle.left(90)
#         # turtle.forward(donnie.y)
#     else:
#         turtle.right(90)
#         # turtle.forward(donnie.y)
# check()

# baht = int(input('Enter cash in Baht: '))
# years = int(input('Enter n years: '))
#
# for i in range(years):
#     list_money = []
#     year_ = i + 1
#     save_acc = baht * (1 + (1.5/100)) ** (year_)
#     list_money.append(save_acc)
#     print(f'You will get back {save_acc:.2f} Baht in {year_} years.')
# if years > 0:
#     final_money = list_money[-1] - baht
# elif years <= 0:
#     final_money = 0
# print(f'At the end, you will earn {final_money:.2f} Baht of interest in {years} years.')

# def read_count_and_sum_x():
#     x = int(input("Enter x: "))
#     ans = -99
#     list_x = []
#     while x != ans:
#         list_x.append(x)
#         x = int(input("Enter x: "))
#     sum_x = sum(list_x)
#     len_x = len(list_x)
#     return sum_x, len_x
#
# print('Round 1:')
# list_sc1 = []
# list_lc1 = []
# sum_x, len_x = read_count_and_sum_x()
# list_sc1.append(sum_x)
# list_lc1.append(len_x)
# #print(list_lc1)
# print(f"Sum of {len_x} x's = {sum_x}")
# print(f"Cumulative sum of {len_x} x's = {sum_x}")
# quit_f = input('Continue or quit (q for quit): ')
# if quit_f == 'q':
#     exit()
# i = 1
# list_s = []
# list_l = []
# print()
# while True:
#     list_s.append(sum_x)
#     list_l.append(len_x)
#     i = i + 1
#     print(f'Round {i}:')
#     sum_x, len_x = read_count_and_sum_x()
#     list_lc1.append(len_x)
#     list_sc1.append(sum_x)
#     list_sum = sum(list_s)
#     list_len = sum(list_l)
#     list_lc1_n = sum(list_lc1)
#     #print(list_lc1)
#     list_sc1_n = sum(list_sc1)
#     print(f"Sum of {len_x} x's = {sum_x}")
#     print(f"Cumulative sum of {list_lc1_n} x's = {list_sc1_n}")
#     quit_f = input('Continue or quit (q for quit): ')
#     if quit_f == 'q':
#         break
#     print()

import ball
import my_event
import turtle
import random
import heapq
import paddle


class BouncingSimulator:
    def __init__(self, num_balls):
        self.num_balls = num_balls
        self.ball_list = []
        self.t = 0.0
        self.pq = []
        self.HZ = 4
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print(self.canvas_width, self.canvas_height)

        ball_radius = 0.05 * self.canvas_width
        for i in range(self.num_balls):
            x = -self.canvas_width + (i + 1) * (2 * self.canvas_width / (self.num_balls + 1))
            y = 0.0
            vx = 10 * random.uniform(-1.0, 1.0)
            vy = 10 * random.uniform(-1.0, 1.0)
            ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.ball_list.append(ball.Ball(ball_radius, x, y, vx, vy, ball_color, i))

        tom = turtle.Turtle()
        self.my_paddle = paddle.Paddle(200, 50, (255, 0, 0), tom)
        self.my_paddle.set_location([0, -50])

        self.screen = turtle.Screen()

    # updates priority queue with all new events for a_ball
    def __predict(self, a_ball):
        if a_ball is None:
            return

        # particle-particle collisions
        for i in range(len(self.ball_list)):
            dt = a_ball.time_to_hit(self.ball_list[i])
            # insert this event into pq
            heapq.heappush(self.pq, my_event.Event(self.t + dt, a_ball, self.ball_list[i], None))

        # particle-wall collisions
        dtX = a_ball.time_to_hit_vertical_wall()
        dtY = a_ball.time_to_hit_horizontal_wall()
        heapq.heappush(self.pq, my_event.Event(self.t + dtX, a_ball, None, None))
        heapq.heappush(self.pq, my_event.Event(self.t + dtY, None, a_ball, None))

    def __draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2 * self.canvas_width)
            turtle.left(90)
            turtle.forward(2 * self.canvas_height)
            turtle.left(90)

    def __redraw(self):
        turtle.clear()
        self.my_paddle.clear()
        self.__draw_border()
        self.my_paddle.draw()
        for i in range(len(self.ball_list)):
            self.ball_list[i].draw()
        turtle.update()
        heapq.heappush(self.pq, my_event.Event(self.t + 1.0 / self.HZ, None, None, None))

    def __paddle_predict(self):
        for i in range(len(self.ball_list)):
            a_ball = self.ball_list[i]
            dtP = a_ball.time_to_hit_paddle(self.my_paddle)
            heapq.heappush(self.pq, my_event.Event(self.t + dtP, a_ball, None, self.my_paddle))

    # move_left and move_right handlers update paddle positions
    def move_left(self):
        if (self.my_paddle.location[0] - self.my_paddle.width / 2 - 40) >= -self.canvas_width:
            self.my_paddle.set_location([self.my_paddle.location[0] - 40, self.my_paddle.location[1]])

    # move_left and move_right handlers update paddle positions
    def move_right(self):
        if (self.my_paddle.location[0] + self.my_paddle.width / 2 + 40) <= self.canvas_width:
            self.my_paddle.set_location([self.my_paddle.location[0] + 40, self.my_paddle.location[1]])

    def run(self):
        # initialize pq with collision events and redraw event
        for i in range(len(self.ball_list)):
            self.__predict(self.ball_list[i])
        heapq.heappush(self.pq, my_event.Event(0, None, None, None))

        # listen to keyboard events and activate move_left and move_right handlers accordingly
        self.screen.listen()
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")

        while (True):
            e = heapq.heappop(self.pq)
            if not e.is_valid():
                continue

            ball_a = e.a
            ball_b = e.b
            paddle_a = e.paddle

            # update positions, and then simulation clock
            for i in range(len(self.ball_list)):
                self.ball_list[i].move(e.time - self.t)
            self.t = e.time

            if (ball_a is not None) and (ball_b is not None) and (paddle_a is None):
                ball_a.bounce_off(ball_b)
            elif (ball_a is not None) and (ball_b is None) and (paddle_a is None):
                ball_a.bounce_off_vertical_wall()
            elif (ball_a is None) and (ball_b is not None) and (paddle_a is None):
                ball_b.bounce_off_horizontal_wall()
            elif (ball_a is None) and (ball_b is None) and (paddle_a is None):
                self.__redraw()
            elif (ball_a is not None) and (ball_b is None) and (paddle_a is not None):
                ball_a.bounce_off_paddle()

            self.__predict(ball_a)
            self.__predict(ball_b)

            # regularly update the prediction for the paddle as its position may always be changing due to keyboard events
            self.__paddle_predict()

        # hold the window; close it by clicking the window close 'x' mark
        turtle.done()


# num_balls = int(input("Number of balls to simulate: "))
num_balls = 10
my_simulator = BouncingSimulator(num_balls)
my_simulator.run()

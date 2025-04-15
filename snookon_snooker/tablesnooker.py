# import turtle
# import math
# turtle.hideturtle()
#
#
# class TableSnooker:
#     # import turtle
#     """screen"""
#     first_layer = turtle.Screen()
#     # first_layer.hideturtle()
#     first_layer.bgcolor('sienna')
#     first_layer.setup(405, 690)
#
#     def __init__(self, h=690, w=405, r=30):
#         if isinstance(h, str):
#             raise TypeError
#         if isinstance(w, str):
#             raise TypeError
#         if isinstance(r, str):
#             raise TypeError
#         import turtle
#         self.h = h
#         self.w = w
#         self.r = r
#         self.balls = []
#         self.cue_ball = None
#         self.cue_stick = None
#         self.shot_strength = 0
#         self.first_layer.listen()
#
#     @property
#     def h(self):
#         return self.h
#
#     @h.setter
#     def h(self, h):
#         if isinstance(h, str):
#             raise TypeError
#         self.h = h
#
#     @property
#     def w(self):
#         return self.w
#
#     @w.setter
#     def w(self, w):
#         if isinstance(w, str):
#             raise TypeError
#         self.w = w
#
#     @property
#     def r(self):
#         return self.r
#
#     @r.setter
#     def r(self, r):
#         if isinstance(r, str):
#             raise TypeError
#         self.r = r
#
#     def border_out(self, color):
#         # import turtle
#         border_out = turtle.Turtle()
#         border_out.hideturtle()
#         border_out.speed(50)
#         # border_out.fillcolor('black')
#         border_out.pensize(5)
#         border_out.penup()
#         border_out.setposition(-h, -w)
#         # border_out.goto(-h, -w)
#         # border_out.setposition(-(1950-x)*1.15, -(y-520)*1.35)
#         border_out.pendown()
#         border_out.color(color)
#         border_out.begin_fill()
#         for size_out in range(2):
#             border_out.forward(1350)
#             border_out.left(90)
#             border_out.forward(820)
#             border_out.left(90)
#         border_out.end_fill()
#
#     def add_ball(self, ball):
#         self.balls.append(ball)
#         if ball.color == "white":  # Set cue_ball as the white ball
#             self.cue_ball = ball
#
#     def pocket(self, h, w, r):
#         # import turtle
#         border_in = turtle.Turtle()
#         border_in.hideturtle()
#         border_in.speed(30)
#         border_in.penup()
#         border_in.setposition(h, w)
#         # border_in.goto(h, w)
#         border_in.pendown()
#         border_in.color('black')
#         border_in.begin_fill()
#         border_in.circle(r)
#         border_in.end_fill()
#
#     def create_cue_stick(self):
#         stick = turtle.Turtle()
#         stick.hideturtle()
#         stick.color('peru')
#         # stick.shapesize(self.h_stick, self.w_stick)
#         stick.penup()
#         stick.setposition(537, 140)
#         # stick.goto(537, 140)
#         stick.pendown()
#         stick.begin_fill()
#         for make_stick in range(2):
#             stick.forward(250)
#             stick.left(90)
#             stick.forward(10)
#             stick.left(90)
#         stick.end_fill()
#         self.cue_stick.goto(self.cue_ball.x, self.cue_ball.y)
#         # self.cue_stick.goto(self.ball_white.x, self.ball_white.y)
#
#     def update_cue_stick(self, x, y):
#         angle = math.degrees(math.atan2(y - self.cue_ball.y, x - self.cue_ball.x))  # Calculate angle
#         self.cue_stick.setheading(angle)
#
#     def shoot(self, x, y):
#         # Calculate the angle and apply force
#         # angle = math.atan2(y - self.ball_white.y, x - self.ball_white.x)
#         angle = math.atan2(y - self.cue_ball.y, x - self.cue_ball.x)
#         speed = 2  # Can change the strength of the shot here
#         self.cue_ball.vx = speed * math.cos(angle)
#         self.cue_ball.vy = speed * math.sin(angle)
#
#     def update(self):
#         for ball in self.balls:
#             ball.move()
#             ball.wall_collision(self.h, self.w)
#             for another in self.balls:
#                 if another != ball and ball.check_collision(another):
#                     ball.handle_collision(another)
#         self.first_layer.update()
#     def close(self):
#         # self.first_layer.onclick(self.on_click)
#         self.first_layer.exitonclick()
#
# h = 690
# w = 405
# r = 30
#
# TableSnooker.border_out(TableSnooker, 'forestgreen')
#
# TableSnooker.pocket(TableSnooker, h - r, w - r, r)  # up right
# TableSnooker.pocket(TableSnooker, -h / 1.02, w - r, r)  # up left
# TableSnooker.pocket(TableSnooker, -h / 1.02, -w - (r * 0.75), r)  # down left
# TableSnooker.pocket(TableSnooker, h - r, -w - (r * 0.75), r)  # down right
# TableSnooker.pocket(TableSnooker, 0, w - (r * 0.3), r)  # center up
# TableSnooker.pocket(TableSnooker, 0, -w - (r * 1.25), r)  # center down
#
# turtle.done()
import turtle
import math
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
screen = turtle.Screen()
screen.bgcolor('sienna')
screen.setup(width=800, height=600)
h = 690
w = 405
r = 30


class TableSnooker:
    def __init__(self, h=600, w=800, pockets=[(660, 375, 30), (-676.47, 375, 30), (-676.47, -427.5, 30),
                                              (660, -427.5, 30), (0, 396, 30), (0, -442.5, 30)]):
        self.h = h
        self.w = w
        self.balls = []
        self.pockets = pockets
        self.first_layer = screen
        self.create_border()

    def create_border(self):
        border_out = turtle.Turtle()
        border_out.hideturtle()
        border_out.speed(50)
        border_out.pensize(5)
        border_out.penup()
        border_out.setposition(-h, -w)
        border_out.pendown()
        border_out.color('green')
        border_out.begin_fill()
        for size_out in range(2):
            border_out.forward(1350)
            border_out.left(90)
            border_out.forward(820)
            border_out.left(90)
        border_out.end_fill()

    def pocket(self, h, w, r):
        border_in = turtle.Turtle()
        border_in.hideturtle()
        border_in.speed(30)
        border_in.penup()
        border_in.setposition(h, w)
        border_in.pendown()
        border_in.color('black')
        border_in.begin_fill()
        border_in.circle(r)
        border_in.end_fill()

    def add_ball(self, ball):
        self.balls.append(ball)

    def remove_ball(self, ball):
        if ball in self.balls:
            self.balls.remove(ball)
            print(f"Ball at ({ball.x}, {ball.y}) has been removed.")

    def check_pocket(self, ball):
        for pocket in self.pockets:
            """pocket[0]=แกนx, pocket[1]=แกนy"""
            dx = ball.x - pocket[0]
            dy = ball.y - pocket[1]
            dist = math.sqrt(dx ** 2 + dy ** 2)
            if dist <= ball.r:
                return True
        return False

    def update(self):
        for ball in self.balls:
            ball.move()
            ball.wall_collision(self.h, self.w)
            if self.check_pocket(ball):
                """check_pocket = True"""
                if ball == ball_white:
                    self.remove_ball(ball)
                    print('Game over')
                    print('white ball gone')
                    exit()
                self.remove_ball(ball)
                print('ball gone')
        screen.update()


class Ball:
    def __init__(self, x, y, r, color, vx=0, vy=0, mass=1):
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy
        self.color = color
        self.mass = mass
        self.ball = turtle.Turtle()
        self.ball.shape('circle')
        self.ball.shapesize(1.5)
        self.ball.color(self.color)
        self.ball.penup()
        self.ball.setposition(self.x, self.y)
        self.count = 0
        self.canvas_width = 800
        self.canvas_height = 600

    def bounce_off_vertical_wall(self):
        self.vx = -self.vx
        self.count += 1

    def bounce_off_horizontal_wall(self):
        self.vy = -self.vy
        self.count += 1

    def bounce_off(self, that):
        dx = that.x - self.x
        dy = that.y - self.y
        dvx = that.vx - self.vx
        dvy = that.vy - self.vy
        dvdr = dx * dvx + dy * dvy;  # dv dot dr
        dist = self.r + that.size  # distance between particle centers at collison

        # magnitude of normal force
        magnitude = 2 * self.mass * that.mass * dvdr / ((self.mass + that.mass) * dist)

        # normal force, and in x and y directions
        fx = magnitude * dx / dist
        fy = magnitude * dy / dist

        # update velocities according to normal force
        self.vx += fx / self.mass
        self.vy += fy / self.mass
        that.vx -= fx / that.mass
        that.vy -= fy / that.mass

        # update collision counts
        self.count += 1
        that.count += 1

    def distance(self, that):
        x1 = self.x
        y1 = self.y
        x2 = that.x
        y2 = that.y
        d = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
        return d

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def time_to_hit(self, that):
        if self is that:
            return math.inf
        dx = that.x - self.x
        dy = that.y - self.y
        dvx = that.vx - self.vx
        dvy = that.vy - self.vy
        dvdr = dx * dvx + dy * dvy
        if dvdr > 0:
            return math.inf
        dvdv = dvx * dvx + dvy * dvy
        if dvdv == 0:
            return math.inf
        drdr = dx * dx + dy * dy
        sigma = self.r + that.size
        d = (dvdr * dvdr) - dvdv * (drdr - sigma * sigma)
        # if drdr < sigma*sigma:
        # print("overlapping particles")
        if d < 0:
            return math.inf
        t = -(dvdr + math.sqrt(d)) / dvdv

        # should't happen, but seems to be needed for some extreme inputs
        # (floating-point precision when dvdv is close to 0, I think)
        if t <= 0:
            return math.inf

        return t

    def time_to_hit_vertical_wall(self):
        if self.vx > 0:
            return (self.canvas_width - self.x - self.r) / self.vx
        elif self.vx < 0:
            return (self.canvas_width + self.x - self.r) / (-self.vx)
        else:
            return math.inf

    def time_to_hit_horizontal_wall(self):
        if self.vy > 0:
            return (self.canvas_height - self.y - self.r) / self.vy
        elif self.vy < 0:
            return (self.canvas_height + self.y - self.r) / (-self.vy)
        else:
            return math.inf

    def time_to_hit_paddle(self, paddle):
        if (self.vy > 0) and ((self.y + self.r) > (paddle.location[1] - paddle.height / 2)):
            return math.inf
        if (self.vy < 0) and ((self.y - self.r) < (paddle.location[1] + paddle.height / 2)):
            return math.inf

        dt = (math.sqrt((paddle.location[1] - self.y) ** 2) - self.r - paddle.height / 2) / abs(self.vy)
        paddle_left_edge = paddle.location[0] - paddle.width / 2
        paddle_right_edge = paddle.location[0] + paddle.width / 2
        if paddle_left_edge - self.r <= self.x + (self.vx * dt) <= paddle_right_edge + self.r:
            return dt
        else:
            return math.inf

    def bounce_off_paddle(self):
        self.vy = -self.vy
        self.count += 1

    # def move(self):
    #     self.x += self.vx
    #     self.y += self.vy
    #     self.ball.setposition(self.x, self.y)
    #
    # def wall_collision(self, table_h, table_w):
    #     table_h = 820
    #     table_w = 1345
    #     if self.x - self.r <= -table_w // 2 or self.x + self.r >= table_w // 2:
    #         self.vx = -self.vx
    #     if self.y - self.r <= -table_h // 2 or self.y + self.r >= table_h // 2:
    #         self.vy = -self.vy
    #
    #     if ball_white.x >= 820 or ball_white.x <= -750:
    #         print('Game over')
    #         print('white ball not in table')
    #         exit()
    #     if ball_white.y >= 1340 or ball_white.y <= -550:
    #         print('Game over')
    #         print('white ball not in table')
    #         exit()
    #
    # def check_collision(self, other):
    #     dist = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    #     if dist <= self.r + other.r:
    #         return True
    #     return False
    #
    # def two_ball_collision(self, other, e=0.9):
    #     dx = other.x - self.x
    #     dy = other.y - self.y
    #     dist = math.sqrt(dx ** 2 + dy ** 2)
    #
    #     if dist == 0:
    #         return
    #
    #     normal_x = dx / dist
    #     normal_y = dy / dist
    #
    #     dvx = self.vx - other.vx
    #     dvy = self.vy - other.vy
    #
    #     dot_product = dvx * normal_x + dvy * normal_y
    #     if dot_product < 0:
    #         pulse = 2 * dot_product / (self.mass + other.mass)
    #
    #         self.vx -= pulse * self.mass * normal_x * e
    #         self.vy -= pulse * self.mass * normal_y * e
    #         other.vx += pulse * other.mass * normal_x * e
    #         other.vy += pulse * other.mass * normal_y * e
    #
    #         overlap = self.r + other.r - dist
    #         self.x -= overlap * normal_x / 2
    #         self.y -= overlap * normal_y / 2
    #         other.x += overlap * normal_x / 2
    #         other.y += overlap * normal_y / 2
    #
    # def apply_drag(self, drag_coefficient=10):
    #     speed = math.sqrt(self.vx ** 2 + self.vy ** 2)
    #     if speed > 0:
    #         drag_force = drag_coefficient * speed
    #         drag_vx = self.vx / speed * drag_force
    #         drag_vy = self.vy / speed * drag_force
    #         self.vx -= drag_vx
    #         self.vy -= drag_vy


class Stick:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.angle = 0
        self.stick = None
        self.create_stick()

    def create_stick(self):
        self.stick = turtle.Turtle()
        self.stick.shape('square')
        self.stick.color('peru')
        self.stick.shapesize(stretch_wid=0.9, stretch_len=10)
        self.stick.penup()
        self.stick.setposition(self.position_x, self.position_y)
        self.stick.setheading(self.angle)

    def update_angle(self, ball_x, ball_y):
        dx = ball_x - self.position_x
        dy = ball_y - self.position_y
        self.angle = math.degrees(math.atan2(dy, dx))
        self.stick.setheading(self.angle)

    def shoot(self, ball, power=5):
        angle_rad = math.radians(self.angle)
        ball.vx = power * math.cos(angle_rad)
        ball.vy = power * math.sin(angle_rad)
        print(f"Shooting ball with velocity: vx={ball.vx}, vy={ball.vy}")


def move_forward():
    stick.position_x += 10
    stick.stick.setposition(stick.position_x, stick.position_y)


def move_backward():
    stick.position_x -= 10
    stick.stick.setposition(stick.position_x, stick.position_y)


def move_up():
    stick.position_y += 10
    stick.stick.setposition(stick.position_x, stick.position_y)


def move_down():
    stick.position_y -= 10
    stick.stick.setposition(stick.position_x, stick.position_y)


# def shoot():
#     global power_list
#     global power
#     power_list = []
#     power = int(input('Enter power of stick: '))
#     power_list.append(power)
#     stick.shoot(ball_white, power_list[0])
#     power_list.clear()

def shoot():
    stick.shoot(ball_white, power=55)


table = TableSnooker()

list_pockets = []

p_1 = TableSnooker.pocket(TableSnooker, h - r, w - r, r)  # up right
p_2 = TableSnooker.pocket(TableSnooker, -h / 1.02, w - r, r)  # up left
p_3 = TableSnooker.pocket(TableSnooker, -h / 1.02, -w - (r * 0.75), r)  # down left
p_4 = TableSnooker.pocket(TableSnooker, h - r, -w - (r * 0.75), r)  # down right
p_5 = TableSnooker.pocket(TableSnooker, 0, w - (r * 0.3), r)  # center up
p_6 = TableSnooker.pocket(TableSnooker, 0, -w - (r * 1.25), r)  # center down

list_pockets.append(p_1)
list_pockets.append(p_2)
list_pockets.append(p_3)
list_pockets.append(p_4)
list_pockets.append(p_5)
list_pockets.append(p_6)
"""black ball"""
ball_black = Ball(-430, 0, 10, 'black')
"""red row 1"""
ball_red_1_1 = Ball(-340, 82, 10, 'darkred')
ball_red_1_2 = Ball(-340, 41, 10, 'darkred')
ball_red_1_3 = Ball(-340, 0, 10, 'darkred')
ball_red_1_4 = Ball(-340, -41, 10, 'darkred')
ball_red_1_5 = Ball(-340, -82, 10, 'darkred')
"""red row 2 x ห่าง 40 y y1+y2/2"""
ball_red_2_1 = Ball(-300, 61, 10, 'darkred')
ball_red_2_2 = Ball(-300, 20.5, 10, 'darkred')
ball_red_2_3 = Ball(-300, -20.5, 10, 'darkred')
ball_red_2_4 = Ball(-300, -61, 10, 'darkred')
"""red row 3"""
ball_red_3_1 = Ball(-260, 40.75, 10, 'darkred')
ball_red_3_2 = Ball(-260, 0, 10, 'darkred')
ball_red_3_3 = Ball(-260, -40.75, 10, 'darkred')
"""red row 4"""
ball_red_4_1 = Ball(-220, 20.375, 10, 'darkred')
ball_red_4_2 = Ball(-220, -20.375, 10, 'darkred')
"""red row 5"""
ball_red_5 = Ball(-180, 0, 10, 'darkred')
"""pink"""
ball_pink = Ball(-137, 0, 10, 'lightpink')
"""blue"""
ball_blue = Ball(107, 0, 10, 'darkblue')
"""in D"""
ball_green = Ball(337, 200, 10, 'limegreen')
ball_orange = Ball(337, 0, 10, 'darkorange')
ball_gold = Ball(337, -200, 10, 'goldenrod')
"""white"""
ball_white = Ball(437, 140, 10, 'white')

table.add_ball(ball_black)
table.add_ball(ball_red_1_1)
table.add_ball(ball_red_1_2)
table.add_ball(ball_red_1_3)
table.add_ball(ball_red_1_4)
table.add_ball(ball_red_1_5)
table.add_ball(ball_red_2_1)
table.add_ball(ball_red_2_2)
table.add_ball(ball_red_2_3)
table.add_ball(ball_red_2_4)
table.add_ball(ball_red_3_1)
table.add_ball(ball_red_3_2)
table.add_ball(ball_red_3_3)
table.add_ball(ball_red_4_1)
table.add_ball(ball_red_4_2)
table.add_ball(ball_red_5)
table.add_ball(ball_pink)
table.add_ball(ball_green)
table.add_ball(ball_blue)
table.add_ball(ball_orange)
table.add_ball(ball_gold)
table.add_ball(ball_white)

stick = Stick(ball_white.x + 150, ball_white.y)

screen.listen()
screen.onkey(move_forward, 'Right')
screen.onkey(move_backward, 'Left')
screen.onkey(move_up, 'Up')
screen.onkey(move_down, 'Down')
screen.onkey(shoot, 'space')


def update():
    table.update()
    stick.update_angle(ball_white.x, ball_white.y)

    for ball in table.balls:
        ball.apply_drag(drag_coefficient=0.05)
    for i in range(len(table.balls)):
        for j in range(i+1, len(table.balls)):
            ball1 = table.balls[i]
            ball2 = table.balls[j]
            if ball1.check_collision(ball2):
                ball1.two_ball_collision(ball2, e=0.9)
    if len(table.balls) == 1 and table.balls == ball_white:
        text_turtle.write('You Win')


screen.tracer(0)
while True:
    update()
    for i, ball in enumerate(table.balls):
        for j in range(i + 1, len(table.balls)):
            if ball.check_collision(table.balls[j]):
                ball.two_ball_collision(table.balls[j])

    screen.update()
screen.bye()


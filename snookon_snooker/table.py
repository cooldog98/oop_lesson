import turtle
import math
turtle.hideturtle()
"""screen"""
first_layer = turtle.Screen()
# first_layer.hideturtle()
first_layer.bgcolor('sienna')
first_layer.setup(405, 690)


class TableSnooker:
    def __init__(self, h=690, w=405, r=30, cue_ball=None):
        self.h = h
        self.w = w
        self.r = r
        self.balls = []
        self.first_layer = first_layer
        self.cue_ball = cue_ball


    def border_out(self, color):
        # import turtle
        border_out = turtle.Turtle()
        border_out.hideturtle()
        border_out.speed(50)
        # border_out.fillcolor('black')
        border_out.pensize(5)
        border_out.penup()
        border_out.setposition(-h, -w)
        # border_out.goto(-h, -w)
        # border_out.setposition(-(1950-x)*1.15, -(y-520)*1.35)
        border_out.pendown()
        border_out.color(color)
        border_out.begin_fill()
        for size_out in range(2):
            border_out.forward(1350)
            border_out.left(90)
            border_out.forward(820)
            border_out.left(90)
        border_out.end_fill()

    def add_ball(self, ball):
        self.balls.append(ball)
        if ball.color == "white":
            self.cue_ball = ball

    def pocket(self, h, w, r):
        # import turtle
        border_in = turtle.Turtle()
        border_in.hideturtle()
        border_in.speed(30)
        border_in.penup()
        border_in.setposition(h, w)
        # border_in.goto(h, w)
        border_in.pendown()
        border_in.color('black')
        border_in.begin_fill()
        border_in.circle(r)
        border_in.end_fill()

    def update(self):
        for ball in self.balls:
            ball.move()
            ball.wall_collision(self.h, self.w)
        self.first_layer.update()

    def close(self):
        # self.first_layer.onclick(self.on_click)
        self.first_layer.exitonclick()


class Ball:
    def __init__(self, x, y, r, color, vx=0, vy=0):
        self.x = x  # X position of the ball
        self.y = y  # y position of the ball
        self.r = r  # radius of the ball
        self.vx = vx    # Velocity in X direction
        self.vy = vy    # Velocity in Y direction
        self.color = color
        self.ball = turtle.Turtle()
        self.ball.hideturtle()
        self.ball.speed(30)
        self.ball.pensize(20)
        self.ball.penup()
        self.ball.setposition(self.x, self.y)
        # self.ball.goto(self.x, self.y)
        self.ball.pendown()
        self.ball.color(self.color)
        self.ball.begin_fill()
        self.ball.circle(self.r)
        self.ball.end_fill()

    def move(self):
        self.x += self.vx
        self.y += self.vy
        # self.ball.setposition(self.x, self.y)
        # self.ball.goto(self.x, self.y)

    def check_collision(self, other):
        dis = math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
        return dis <= self.r + other.r

    def handle_collision(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        distant = math.sqrt(dx**2 + dy**2)
        normal_x = dx/distant
        normal_y = dy/distant
        dvx = self.vx - other.vx
        dvy = self.vy - other.vy
        dot_product = dvx * normal_x + dvy * normal_y
        if dot_product < 0:
            pulse = 2 * dot_product / (self.r + other.r)
            self.vx -= pulse * self.r * normal_x
            self.vy -= pulse * self.r * normal_y
            other.vx += pulse * self.r * normal_x
            other.vy += pulse * self.r * normal_y

    def wall_collision(self, table_h=690, table_w=405):
        if self.x - self.r <= -table_w / 2 or self.x + self.r >= table_w / 2:
            self.vx = -self.vx
        if self.y - self.r <= -table_h/2 or self.y + self.r >= table_h/2:
            self.vy = -self.vy


class Stick:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.angle = 0  # Angle in degrees
        self.stick = None
        self.create_stick()

    def create_stick(self):
        self.stick = turtle.Turtle()
        self.stick.hideturtle()
        self.stick.color('peru')
        self.stick.penup()
        self.stick.setposition(self.position_x, self.position_y)
        self.stick.pendown()
        self.stick.shape("square")
        self.stick.shapesize(stretch_wid=0.9, stretch_len=13)
        self.stick.setheading(self.angle)
        self.stick.showturtle()

    def move_forward(self):
        self.stick.penup()
        self.position_x += 5
        self.stick.setposition(self.position_x, self.position_y)

    def move_backward(self):
        self.stick.penup()
        self.position_x -= 5
        self.stick.setposition(self.position_x, self.position_y)

    def move_up(self):
        self.stick.penup()
        self.stick.penup()
        self.position_y += 5
        self.stick.setposition(self.position_x, self.position_y)

    def move_down(self):
        self.stick.penup()
        self.stick.penup()
        self.position_y -= 5
        self.stick.setposition(self.position_x, self.position_y)

    def update_angle(self, ball_x, ball_y):
        self.stick.penup()
        # Calculate angle between cue ball and stick
        dx = ball_x - self.position_x
        dy = ball_y - self.position_y
        self.angle = math.degrees(math.atan2(dy, dx))
        self.stick.setheading(self.angle)

    def shoot(self, ball, power=5):
        angle_rad = math.radians(self.angle)
        ball.vx = power * math.cos(angle_rad)
        ball.vy = power * math.sin(angle_rad)
        print(f"Ball velocity: vx={ball.vx}, vy={ball.vy}")


if __name__ == "__main__":
    h = 690
    w = 405
    r = 30

    TableSnooker.border_out(TableSnooker, 'forestgreen')

    TableSnooker.pocket(TableSnooker, h - r, w - r, r)  # up right
    TableSnooker.pocket(TableSnooker, -h / 1.02, w - r, r)  # up left
    TableSnooker.pocket(TableSnooker, -h / 1.02, -w - (r * 0.75), r)  # down left
    TableSnooker.pocket(TableSnooker, h - r, -w - (r * 0.75), r)  # down right
    TableSnooker.pocket(TableSnooker, 0, w - (r * 0.3), r)  # center up
    TableSnooker.pocket(TableSnooker, 0, -w - (r * 1.25), r)  # center down

    """black"""
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
    ball_red_5 = Ball(-180, -0, 10, 'darkred')

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

    table = TableSnooker(h, w, r)

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

    stick_use = Stick(ball_white.x + 50, ball_white.y)
    stick_use.stick
    table = TableSnooker(h, w, r)
    def update_stick():
        stick_use.update_angle(437, 140)

    def move_forward():
        stick_use.move_forward()

    def move_backward():
        stick_use.move_backward()

    def move_up():
        stick_use.move_up()

    def move_down():
        stick_use.move_down()

    def shoot():
        stick_use.shoot(ball_white, power=5)


    # Set controls
    table.first_layer.listen()
    table.first_layer.onkey(move_forward, 'Right')
    table.first_layer.onkey(move_backward, 'Left')
    table.first_layer.onkey(move_up, 'Up')
    table.first_layer.onkey(move_down, 'Down')
    table.first_layer.onkey(shoot, 'space')

    while True:
        # Update balls and stick
        for ball in table.balls:
            ball.move()
            ball.wall_collision()

        # Check ball collisions
        for i, ball in enumerate(table.balls):
            for j in range(i + 1, len(table.balls)):
                if ball.check_collision(table.balls[j]):
                    ball.handle_collision(table.balls[j])

        # Update the game state
        stick_use.update_angle(ball_white.x, ball_white.y)
        table.update()

        # Refresh the screen
        turtle.update()

    turtle.done()

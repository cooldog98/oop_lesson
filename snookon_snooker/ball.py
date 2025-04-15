import turtle
turtle.hideturtle()
import math
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

    # def ball(self):
    #     import turtle
    #     ball = turtle.Turtle()
    #     ball.speed(30)
    #     ball.pensize(20)
    #     ball.penup()
    #     ball.setposition(self.x, self.y)
    #     ball.pendown()
    #     ball.color(self.color)
    #     ball.begin_fill()
    #     ball.circle(self.r)
    #     ball.end_fill()
    #     ball.hideturtle()

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.ball.setposition(self.x, self.y)
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

    def wall_collision(self, table_h= 690, table_w=405):
        if self.x - self.r <= -table_w / 2 or self.x + self.r >= table_w / 2:
            self.vx = -self.vx
        if self.y - self.r <= -table_h/2 or self.y + self.r >= table_h/2:
            self.vy = -self.vy



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

turtle.done()

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
# """black"""
# ball_black = Ball(-430, 0, 10, 'black')
# """red row 1"""
# ball_red_1_1 = Ball(-340, 82, 10, 'darkred')
# ball_red_1_2 = Ball(-340, 41, 10, 'darkred')
# ball_red_1_3 = Ball(-340, 0, 10, 'darkred')
# ball_red_1_4 = Ball(-340, -41, 10, 'darkred')
# ball_red_1_5 = Ball(-340, -82, 10, 'darkred')
# """red row 2 x ห่าง 40 y y1+y2/2"""
# ball_red_2_1 = Ball(-300, 61, 10, 'darkred')
# ball_red_2_2 = Ball(-300, 20.5, 10, 'darkred')
# ball_red_2_3 = Ball(-300, -20.5, 10, 'darkred')
# ball_red_2_4 = Ball(-300, -61, 10, 'darkred')
# """red row 3"""
# ball_red_3_1 = Ball(-260, 40.75, 10, 'darkred')
# ball_red_3_2 = Ball(-260, 0, 10, 'darkred')
# ball_red_3_3 = Ball(-260, -40.75, 10, 'darkred')
# """red row 4"""
# ball_red_4_1 = Ball(-220, 20.375, 10, 'darkred')
# ball_red_4_2 = Ball(-220, -20.375, 10, 'darkred')
# """red row 5"""
# ball_red_5 = Ball(-180, -0, 10, 'darkred')
# """pink"""
# ball_pink = Ball(-137, 0, 10, 'lightpink')
# """blue"""
# ball_blue = Ball(107, 0, 10, 'darkblue')
# """in D"""
# ball_green = Ball(337, 200, 10, 'limegreen')
# ball_orange = Ball(337, 0, 10, 'darkorange')
# ball_gold = Ball(337, -200, 10, 'goldenrod')
# """white"""
# ball_white = Ball(437, 140, 10, 'white')
#
# Ball.stick(Ball, ball_white.x + 50, ball_white.y)
#
# turtle.done()
#
# TableSnooker.add_ball(Ball, ball_black)
# TableSnooker.add_ball(Ball, ball_red_1_1)
# TableSnooker.add_ball(Ball, ball_red_1_2)
# TableSnooker.add_ball(Ball, ball_red_1_3)
# TableSnooker.add_ball(Ball, ball_red_1_3)
# TableSnooker.add_ball(Ball, ball_red_1_4)
# TableSnooker.add_ball(Ball, ball_red_1_5)
# TableSnooker.add_ball(Ball, ball_red_2_1)
# TableSnooker.add_ball(Ball, ball_red_2_2)
# TableSnooker.add_ball(Ball, ball_red_2_3)
# TableSnooker.add_ball(Ball, ball_red_2_4)
# TableSnooker.add_ball(Ball, ball_red_3_1)
# TableSnooker.add_ball(Ball, ball_red_3_2)
# TableSnooker.add_ball(Ball, ball_red_3_3)
# TableSnooker.add_ball(Ball, ball_red_4_1)
# TableSnooker.add_ball(Ball, ball_red_4_2)
# TableSnooker.add_ball(Ball, ball_red_5)
# TableSnooker.add_ball(Ball, ball_pink)
# TableSnooker.add_ball(Ball, ball_green)
# TableSnooker.add_ball(Ball, ball_blue)
# TableSnooker.add_ball(Ball, ball_orange)
# TableSnooker.add_ball(Ball, ball_gold)
# TableSnooker.add_ball(Ball, ball_white)

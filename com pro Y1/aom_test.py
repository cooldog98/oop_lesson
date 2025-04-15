# import turtle
# import random
#
# choice = int(input('Which art do you want to generate?'
#                    '\nEnter a number between 1 to 9 inclusive: '))
#
#
# class Turtle:
#     def __init__(self, choice):
#         self.num_side = self.num_side()
#         self.size = random.randint(50, 150)
#         self.orientation = random.randint(0, 90)
#         self.location = [random.randint(-300, 300), random.randint(-200, 200)]
#         self.border_size = random.randint(1, 10)
#         self.color = self.get_new_color()
#         self.reduction_ratio = 0.618
#         self.choice = choice
#
#     def num_side(self):
#         if choice in [1, 2, 3]:
#             num_side = choice + 2
#             self.choice = num_side
#             return self.choice
#
#         elif choice in [4, 8, 9]:
#             num_side = random.randint(3, 5)
#             self.choice = num_side
#             return self.choice
#
#         else:
#             num_side = choice - 2
#             self.choice = num_side
#             return self.choice
#
#     def other_choice(self):
#         turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
#         turtle.left(90)
#         turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
#         turtle.right(90)
#         self.location[0] = turtle.pos()[0]
#         self.location[1] = turtle.pos()[1]
#         self.size *= self.reduction_ratio
#         turtle.penup()
#
#     def draw(self):
#         for i in range(3):
#             self.draw_polygon()
#             if choice == 9:
#                 self.other_choice()
#             elif 5 <= choice <= 9:
#                 self.other_choice()
#
#     def draw_polygon(self):
#         turtle.penup()
#         turtle.goto(self.location[0], self.location[1])
#         turtle.setheading(self.orientation)
#         turtle.color(self.color)
#         turtle.pensize(self.border_size)
#         turtle.pendown()
#         for _ in range(self.num_side):
#             turtle.forward(self.size)
#             turtle.left(360 / self.num_side)
#         turtle.penup()
#
#     def get_new_color(self):
#         self.new_color = (random.randint(0, 255), random.randint(0, 255)
#                           , random.randint(0, 255))
#         return self.new_color
#
#     turtle.speed(0)
#     turtle.bgcolor('black')
#     turtle.tracer(0)
#     turtle.colormode(255)
#
#
# if 1 <= choice <= 8:
#     for i in range(25):
#         drawing = Turtle(choice)
#         drawing.draw()
# if choice == 9:
#     for i in range(8):
#         for j in range(5):
#             drawing = Turtle(choice)
#             drawing.draw()
#         drawing = Turtle(choice)
#         drawing.draw_polygon()
# turtle.done()

import turtle
import random
screen_turtle = turtle.Turtle()
screen_turtle.hideturtle()
turtle.hideturtle()


class Paddle:
    def __init__(self):
        self.paddle = turtle.Turtle()
        self.paddle.shape("square")
        self.paddle.color("DodgerBlue4")
        self.paddle.shapesize(stretch_wid=1, stretch_len=6)
        self.paddle.penup()
        self.paddle.goto(0, -250)

    def move_left(self):
        x = self.paddle.xcor() - 25
        self.paddle.setx(max(x, -350))
        # print("left")

    def move_right(self):
        x = self.paddle.xcor() + 25
        self.paddle.setx(min(x, 350))
        # print("right")


class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.shape("circle")
        self.ball.color("DarkGoldenrod")
        self.ball.penup()
        self.ball.speed(0)
        self.ball.circle(20)
        self.ball.goto(0, -200)
        self.dx_ball = random.choice([3, -3])
        self.dy_ball = 3

    def move(self):
        self.ball.setx(self.ball.xcor() + self.dx_ball)
        self.ball.sety(self.ball.ycor() + self.dy_ball)

    def bounce_x(self):
        self.dx_ball *= -1

    def bounce_y(self):
        self.dy_ball *= -1


class Brick:
    def __init__(self, x, y, color):
        self.brick = turtle.Turtle()
        self.brick.shape("circle")  # Changed to circle
        self.brick.color(color)
        self.brick.shapesize(stretch_wid=1.5, stretch_len=1.5)  # Adjusted for circle size
        self.brick.penup()
        self.brick.goto(x, y)

    def hide(self):
        self.brick.hideturtle()

    def is_visible(self):
        return self.brick.isvisible()


class Bomb:
    def __init__(self, x, y):
        self.bomb = turtle.Turtle()
        self.bomb.shape("circle")
        self.bomb.color("firebrick4")
        self.bomb.penup()
        self.bomb.goto(x, y)
        self.dy = -3

    def move(self):
        self.bomb.sety(self.bomb.ycor() + self.dy)

    def is_out_of_bounds(self):
        return self.bomb.ycor() < -300


class Star: #test
    def __init__(self, x, y, color="peru", size=20):
        self.size = size
        self.star = turtle.Turtle()
        self.star.shape('square')
        # self.star.hideturtle()
        self.color = color
        self.star.penup()
        self.star.goto(x, y)
        # self.star.pendown()
        self.dy_star = -1.8
        # self.draw_star()

    # def draw_star(self):
    #     self.star.color(self.color)
    #     #self.star.hideturtle()
    #     self.star.pendown()
    #     self.star.begin_fill()
    #     self.star.right(75)
    #     self.star.forward(self.size)
    #     for i in range(4):
    #         self.star.right(144)
    #         self.star.forward(self.size)
    #     self.star.end_fill()
    #     self.star.penup()
        # self.star.tracer(1)

    def move(self):
        self.star.sety(self.star.ycor() + self.dy_star)

    def is_out_of_bounds(self):
        return self.star.ycor() < -300


class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("BOMB Bouncing")
        self.screen.bgcolor("PaleGoldenrod")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)

        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = []
        self.bombs = []
        self.star = []
        self.score = 0

        self.score_display = turtle.Turtle()
        self.score_display.color("black")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(0, 260)
        self.update_score(0)

        self.create_bricks()
        # self.setup_controls()

    def input_name(self):
        turtle.penup()
        turtle.goto(0, 150)
        turtle.write("Hello, what's your name?", align="center", font=("Arial", 16, "bold"))

        self.name = self.screen.textinput("Your name", "Name")
        if not self.name:
            self.name = "Player"
        turtle.clear()


    def create_bricks(self):
        colors = [ "SteelBlue2","SkyBlue3", "SkyBlue4", "SteelBlue4",
                  "DodgerBlue4"]
        for row in range(5):
            for col in range(24):
                x = -400 + col * 35
                y = 230 - row * 35
                color = colors[row % len(colors)]
                self.bricks.append(Brick(x, y, color))

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(self.paddle.move_left, "Left")
        self.screen.onkey(self.paddle.move_right, "Right")

    def update_score(self, points):
        self.score += points
        self.score_display.clear()
        self.score_display.write(f"Score : {self.score}", align="center", font=("Arial", 20, "normal"))

    def drop_bomb(self, x, y):
        self.bombs.append(Bomb(x, y))

    # def drop_star(self, x, y):
    #     self.star.append(Star(x, y))
    def drop_star(self, x, y):
        new_star = Star(x, y)
        self.star.append(new_star)

    def play(self):
        game_over = False
        self.input_name()

        while not game_over:
            self.setup_controls()
            self.screen.update()
            self.ball.move()

            # Ball collision with walls
            if self.ball.ball.xcor() > 390 or self.ball.ball.xcor() < -390:
                self.ball.bounce_x()

            if self.ball.ball.ycor() > 290:
                self.ball.bounce_y()

            # Ball collision with paddle
            if (self.ball.ball.ycor() - 13.5 < -240 and self.ball.ball.ycor() - 13.5 > -250) and \
                    (self.paddle.paddle.xcor() - 100 < self.ball.ball.xcor() - 13.5 < self.paddle.paddle.xcor() + 100):
                self.ball.bounce_y()

            # Ball collision with bricks
            for brick in self.bricks:
                if brick.is_visible() and \
                        (brick.brick.xcor() - 20 < self.ball.ball.xcor() < brick.brick.xcor() + 20) and \
                        (brick.brick.ycor() - 20 < self.ball.ball.ycor() < brick.brick.ycor() + 20):
                    brick.hide()
                    self.bricks.remove(brick)
                    self.ball.bounce_y()
                    self.update_score(10)

                    # Drop bomb with 30% chance
                    if random.random() < 0.30:
                        self.drop_bomb(brick.brick.xcor(), brick.brick.ycor())
                        break

                    if random.random() < 0.70:
                        self.drop_star(brick.brick.xcor(), brick.brick.ycor())
                        break

            # Check for game win
            if not self.bricks:
                self.win()

            # Check if ball falls below the paddle
            if self.ball.ball.ycor() < -300:
                game_over = True
                self.end_out()

            # Move star
            for star in self.star:
                star.move()
                turtle.update()

                # Remove star if it falls out of bounds
                if star.is_out_of_bounds():
                    star.star.hideturtle()
                    self.star.remove(star)

                # star collision with paddle
                if (star.star.ycor() - 13.5 < -240 and star.star.ycor() - 13.5 > -250) and \
                        (self.paddle.paddle.xcor() - 100 < star.star.xcor() - 13.5 < self.paddle.paddle.xcor() + 100):
                    self.update_score(30)  # เพิ่มคะแนน
                    star.star.hideturtle()
                    self.star.remove(star)

            # Move bombs
            for bomb in self.bombs:
                bomb.move()

                # Remove bomb if it falls out of bounds
                if bomb.is_out_of_bounds():
                    bomb.bomb.hideturtle()
                    self.bombs.remove(bomb)

                # Bomb collision with paddle
                if (bomb.bomb.ycor() - 13.5 < -240 and bomb.bomb.ycor() - 13.5> -250) and \
                        (self.paddle.paddle.xcor() - 100 < bomb.bomb.xcor() - 13.5 < self.paddle.paddle.xcor() + 100):
                    self.end_bomb()
                    game_over = True

    def end_bomb(self):
        self.screen.clear()
        self.screen.bgcolor("cornsilk2")
        game_over_text = turtle.Turtle()
        game_over_text.color("DarkRed")
        game_over_text.hideturtle()
        game_over_text.write(f"\nGame Over! \n \nBomb hit the paddle\n \n{self.name}'s "
                             f"Score: {self.score}", align="center", font=("Arial", 36, "bold"))
        self.screen.mainloop()

    def end_out(self):
        self.screen.clear()
        self.screen.bgcolor("cornsilk2")
        game_over_text = turtle.Turtle()
        game_over_text.color("DarkRed")
        game_over_text.hideturtle()
        game_over_text.write(f"\nGame Over!\n \nYou missed the ball\n \n{self.name}'s "
                             f"Score: {self.score}", align="center", font=("Arial", 36, "bold"))
        self.screen.mainloop()

    def win(self): #new
        self.screen.clear()
        self.screen.bgcolor("DarkGoldenrod2")
        game_over_text = turtle.Turtle()
        game_over_text.color("DarkRed")
        game_over_text.hideturtle()
        game_over_text.write(f"\n{self.name} WIN\n \nFinal Score: {self.score}",
                             align="center", font=("Arial", 36, "bold"))
        self.screen.mainloop()

game = Game()
game.play()

Snookong Snooker: A Simple Snooker Game

This project is a snooker game where the objective is to clear all the balls on the table, leaving only the white ball. 
However, if the white ball falls into a pocket or goes off the table, the game ends.

# Project Description
This is a Snooker Game created using Python's Turtle graphics. The game simulates a snooker table with balls, pockets, 
and player interactions. Players control the cue stick to hit the white ball and interact with other balls on the table.
The game includes features like ball movement, collisions, bouncing off walls, and detecting when balls fall into pockets.
0o
# To run this project, follow the steps below:
1. Install Python 3.x: Make sure Python is installed on your machine. 
You can download it from the official website: https://www.python.org/downloads/
2. Install Required Libraries: The project uses the turtle library, which comes pre-installed with Python. 
Therefore, no additional libraries are needed.
3. Clone the Repository: Clone this repository to your local machine:
git clone https://github.com/your-username/snooker-game-simulation.git
cd snooker-game-simulation
4. Run the Game: Run the project script using the following command:
python snooker_game.py

# Usage
Once the game is running, you can control the cue stick and balls using the following keypresses:
Arrow Keys: Move the cue stick (Up, Down, Left, Right).
Space bar: Shoot the white ball with the cue stick.
Expected Outputs:
1. When the ball moves, its new position will be reflected on the screen.
2. If the white ball falls into a pocket, the game will end with a "Game Over" message in terminal.
3. If you pocket any other balls, they will disappear, and a message will be printed to the terminal.

# link VDO

# UML
(picture in UML.png)
+-----------------+
|   TableSnooker |
+-----------------+
| - h: int        |
| - w: int        |
| - balls: list   |
| - pockets: list |
| - first_layer: Screen |
+-----------------+
| + __init__(h, w, pockets) |
| + create_border() |
| + pocket(h, w, r) |
| + add_ball(ball) |
| + remove_ball(ball) |
| + check_pocket(ball): bool |
| + update()       |
+-----------------+

           ^
           |
           |
+----------------+
|      Ball      |
+----------------+
| - x: float     |
| - y: float     |
| - r: float     |
| - vx: float    |
| - vy: float    |
| - color: str   |
| - mass: float  |
| - ball: Turtle |
+----------------+
| + __init__(x, y, r, color, vx, vy, mass) |
| + move()       |
| + wall_collision(table_h, table_w) |
| + check_collision(other: Ball): bool |
| + two_ball_collision(other, e) |
| + apply_drag(drag_coefficient)  |
+----------------+

           ^
           |
           |
+-------------------+
|       Stick       |
+-------------------+
| - position_x: float |
| - position_y: float |
| - angle: float      |
| - stick: Turtle     |
+-------------------+
| + __init__(position_x, position_y) |
| + create_stick() |
| + update_angle(ball_x, ball_y) |
| + shoot(ball, power) |
+-------------------+

# Class TableSnooker
1. create_border = make the green section of the table
2. pocket(h, w, r) = make pocket
3. add_ball(ball) = add ball to balls (list of ball that still in table)
4. remove_ball(ball) = remove the ball and make the ball disappear form screen
5. check_pocket(ball): bool = check the ball that hti the pocket or not by use physics formular return True or False
6. update() = be the function that call some of def in this class and in Ball class to work.

# Class Ball
1. move() = move the ball
2. wall_collision(table_h, table_w) = if the ball collision the wall make it bounce back and if the white ball
out of the table the game will over
3. check_collision(other: Ball): bool = check that the ball hit each other or not return Ture or False
4. two_ball_collision(other, e) = about physics when the ball collision another ball what happen after that
5. apply_drag(drag_coefficient) = make the ball slower after hit another already

# Class Stick
1. create_stick() = make stick
2. update_angle(ball_x, ball_y) = function calculates the angle between the cue stick and the ball based on their 
relative positions, and then updates the cue stick's heading so that it faces the ball. 
This ensures that the cue stick is always correctly aligned with the ball, allowing for accurate shooting.
3. shoot(ball, power) = The function calculates the direction and velocity of the ball based on the angle of 
the cue stick and the power selected by the player. It then sets the velocity components in the x and y directions 
to make the ball move in the direction the cue stick is pointing.


# Features
1. Physics-based Ball Movement: The balls move based on velocity and collide with other balls and walls.
2. Pockets: Six pockets on the table where balls can fall.
3. Cue Stick: A player-controlled cue stick to strike the white ball.
4. Collision Detection: Balls interact with each other and walls.
5. Drag and Friction: Balls experience drag and friction over time.
6. Game Over: The game ends if the white ball falls into any pocket.

![img.png](img.png)

# While the game is playable, there are some bugs:
 1. White Ball Interaction:
 • Sometimes, when the white ball hits another ball, the other ball does not move
 2. White Ball Falling Off the Table:
 • If the white ball is shot repeatedly at the edge of the table, it can fall off entirely.
 3. Ball in Pocket Issue:
 • Occasionally, when a ball falls into a pocket, it bounces back onto the table instead of being removed. 
   Can try by use white ball because it easy to look if the white ball falls into a pocket, the game screen 
   will close immediately.
 4. Power Input Functionality:
 • A feature was tested where players could input the shooting power using turtle.textinput(). 
   However, after entering the input, the stick became unresponsive.
 • Switching to Python’s standard input() resolved this issue, but it requires the game to be played 
   in full-screen mode, which could make gameplay inconvenient.
import turtle
import ball

try:
    num_balls = int(input("Number of balls to simulate: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
turtle.colormode(255)
color_list = []
xpos = []
ypos = []
vx = []
vy = []
ball_color = []

# Initialize ball positions, velocities, and colors
ball.initialize(xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls)

while True:
    turtle.clear()
    for i in range(num_balls):
        ball.draw_circle(ball_color[i], ball_radius, xpos[i], ypos[i])
        ball.move_circle(i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius)
    turtle.update()

# Hold the window; close it by clicking the window close 'x' mark
turtle.done()


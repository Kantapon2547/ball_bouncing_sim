import turtle
import random


def draw_circle(color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()


def move_circle(i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius):
    xpos[i] += vx[i]
    ypos[i] += vy[i]

    if abs(xpos[i] + vx[i]) > (canvas_width - ball_radius):
        vx[i] = -vx[i]

    if abs(ypos[i] + vy[i]) > (canvas_height - ball_radius):
        vy[i] = -vy[i]


def initilizing(xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls):
    for i in range(num_balls):
        xpos.append(random.randint(-1*canvas_width + ball_radius, canvas_width - ball_radius))
        ypos.append(random.randint(-1*canvas_height + ball_radius, canvas_height - ball_radius))
        vx.append(random.randint(1, 0.01*canvas_width))
        vy.append(random.randint(1, 0.01*canvas_height))
        ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

import turtle
import random


class Ball:
    def __init__(self, canvas_width, canvas_height, ball_radius):
        self.xpos = random.uniform(-canvas_width / 2 + ball_radius, canvas_width / 2 - ball_radius)
        self.ypos = random.uniform(-canvas_height / 2 + ball_radius, canvas_height / 2 - ball_radius)
        self.vx = random.uniform(1, 0.01 * canvas_width)
        self.vy = random.uniform(1, 0.01 * canvas_height)
        self.ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.ball_radius = ball_radius

    def draw_circle(self):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.ball_color)
        turtle.fillcolor(self.ball_color)
        turtle.goto(self.xpos, self.ypos)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.ball_radius)
        turtle.end_fill()

    def move_circle(self, canvas_width, canvas_height, ball_radius):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.xpos += self.vx
        self.ypos += self.vy

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos + self.vx) > (canvas_width - ball_radius):
            self.vx = -self.vx

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos + self.vy) > (canvas_height - ball_radius):
            self.vy = -self.vy


class Simulation:
    def __init__(self, num_balls, canvas_width, canvas_height, ball_radius):
        self.balls = [Ball(canvas_width, canvas_height, ball_radius) for _ in range(num_balls)]

    def run(self):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)

        while True:
            turtle.clear()
            for ball in self.balls:
                ball.draw_circle()
                ball.move_circle(canvas_width, canvas_height, ball_radius)
            turtle.update()


if __name__ == "__main__":
    num_balls = int(input("Number of balls to simulate: "))
    canvas_width = turtle.screensize()[0]
    canvas_height = turtle.screensize()[1]
    ball_radius = 0.05 * canvas_width

    simulation = Simulation(num_balls, canvas_width, canvas_height, ball_radius)
    simulation.run()
    turtle.done()
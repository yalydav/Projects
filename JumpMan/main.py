import turtle
import time
import random

delay = 0.05


class Game:
    def __init__(self):
        self.delay = 0.05
        self.Score = 0
        self.char_color = None
        self.ball_color = None
        self.wn = None
        self.char = None
        self.ball = None
        self.cloud = None
        self.floor = None
        self.pen = None

    def set_colors(self):
        # function asks and sets what color the user wants the ball and character
        answer = input("character color?\n")
        if answer == "white":
            self.char_color = "white"
        elif answer == "red":
            self.char_color = "red"
        elif answer == "blue":
            self.char_color = "blue"
        elif answer == "yellow":
            self.char_color = "yellow"
        elif answer == "pink":
            self.char_color = "pink"
        else:
            self.char_color = "black"
        print("set char color successfully")

        # Ball color
        answer = input("ball color?\n")
        if answer == "white":
            self.ball_color = "white"
        elif answer == "red":
            self.ball_color = "red"
        elif answer == "blue":
            self.ball_color = "blue"
        elif answer == "yellow":
            self.ball_color = "yellow"
        elif answer == "pink":
            self.ball_color = "pink"
        else:
            self.ball_color = "white"
        print("set ball color successfully")

    def create_and_set_screen(self):
        self.wn = turtle.Screen()
        self.wn.title("FUN GAME")
        self.wn.bgcolor("cyan")
        self.wn.tracer(0)
        self.wn.setup(width=600, height=600)

    def create_and_set_floor(self):
        self.floor = turtle.Turtle()
        self.floor.speed(0)
        self.floor.shape("square")
        self.floor.color("orange")
        self.floor.shapesize(7, 30)
        self.floor.penup()
        self.floor.goto(0, -280)
        self.floor.direction = "stop"

    def create_and_set_character(self):
        self.char = turtle.Turtle()
        self.char.speed(0)
        self.char.shape("square")
        self.char.color(self.char_color)
        self.char.shapesize(2, 1)
        self.char.penup()
        self.char.goto(0, -190)
        self.char.direction = "stop"

    def create_and_set_ball(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color(self.ball_color)
        self.ball.penup()
        self.ball.goto(0, -130)

    def create_and_set_clouds(self, xpos):
        # Cloud1
        self.cloud = turtle.Turtle()
        self.cloud.speed(0)
        self.cloud.shape("square")
        self.cloud.color("white")
        self.cloud.shapesize(1, 3)
        self.cloud.penup()
        self.cloud.goto(xpos, 200)
        self.cloud.direction = "stop"

        # Cloud2
        self.cloud = turtle.Turtle()
        self.cloud.speed(0)
        self.cloud.shape("square")
        self.cloud.color("white")
        self.cloud.shapesize(1, 5)
        self.cloud.penup()
        self.cloud.goto(xpos, 190)
        self.cloud.direction = "stop"

        # Cloud3
        self.cloud = turtle.Turtle()
        self.cloud.speed(0)
        self.cloud.shape("square")
        self.cloud.color("white")
        self.cloud.shapesize(1, 3)
        self.cloud.penup()
        self.cloud.goto(xpos, 180)
        self.cloud.direction = "stop"

    def create_and_set_score(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("black")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

    def check_char_touch_with_ball(self):
        if self.char.distance(self.ball) < 25:
            x = (random.randint(-290, 290))
            y = (-130)
            self.ball.goto(x, y)

            # Increase the score
            self.Score += 10
            self.pen.clear()
            self.pen.write("Score: {}".format(self.Score), align="center", font=("Courier", 24, "normal"))

    def go_up(self):
        self.char.direction = "up"
        self.move()

    def go_left(self):
        self.char.direction = "left"
        self.move()

    def go_right(self):
        self.char.direction = "right"
        self.move()

    def move(self):
        if self.char.direction == "up":
            # on ground (d = 60)
            y = self.char.ycor()
            self.char.sety(y + 20)
            self.wn.update()
            y = self.char.ycor()
            time.sleep(delay)
            self.char.sety(y + 20)
            self.wn.update()
            # air time !!!! d can be 20. How can we know? checkTouch() function
            self.check_char_touch_with_ball()
            # --------------------

            # air time delay
            time.sleep(0.05)
            y = self.char.ycor()
            self.char.sety(y - 20)
            self.wn.update()
            y = self.char.ycor()
            time.sleep(delay)
            self.char.sety(y - 20)
            # on ground (d = 60)

        if self.char.direction == "left":
            x = self.char.xcor()
            self.char.setx(x - 20)

        if self.char.direction == "right":
            x = self.char.xcor()
            self.char.setx(x + 20)

    def keyboard_moving_char(self):
        self.wn.listen()
        self.wn.onkeypress(self.go_up, "space")
        self.wn.onkeypress(self.go_left, "Left")
        self.wn.onkeypress(self.go_right, "Right")

    def main_game_loop(self):
        while True:
            self.wn.update()

            # Don't pass the border!!
            if self.char.xcor() > 290:
                self.char.goto(-290, -190)

            if self.char.xcor() < -290:
                self.char.goto(290, -190)

            time.sleep(delay)


def main():
    JumpMan = Game()  # create memory area
    JumpMan.set_colors()  # set char & ball colors
    JumpMan.create_and_set_screen()  # create and set screen
    JumpMan.create_and_set_character()  # create and set character
    JumpMan.create_and_set_ball()  # create and set ball
    JumpMan.create_and_set_floor()  # create and set floor
    JumpMan.create_and_set_clouds(0)  # middle cloud
    JumpMan.create_and_set_clouds(150)  # right cloud
    JumpMan.create_and_set_clouds(-150)  # left cloud
    JumpMan.create_and_set_score()  # create and set score
    JumpMan.keyboard_moving_char()  # w a d moving char
    JumpMan.main_game_loop()  # game rules and game setup


main()

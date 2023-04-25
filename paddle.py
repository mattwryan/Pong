from turtle import Turtle

STRETCH_WIDTH = 5
STRETCH_LENGTH = 1

class Paddle(Turtle):
    #NOTE: To give a class parameter a default value, assign it in the init method parameters
    def __init__(self, starting_x=350, starting_y=0):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LENGTH)
        self.penup()
        self.goto(starting_x, starting_y)


    def paddle_up(self):
        if self.ycor() >= 240:
            pass
        else:
            self.goto(self.xcor(), self.ycor() + 20)


    def paddle_down(self):
        if self.ycor() <= -240:
            pass
        else:
            self.goto(self.xcor(), self.ycor() - 20)

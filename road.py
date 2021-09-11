from turtle import Turtle


class Road():
    def __init__(self):
        self.tim = Turtle()
        self.tim.pencolor("yellow")
        self.create_road()



    def create_road(self):
        for y in range(-260, 300, 40):
            self.tim.penup()
            self.tim.goto(320,y)
            self.tim.pendown()
            self.tim.goto(-320,y)

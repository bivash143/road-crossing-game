from turtle import Turtle


class Road():
    def __init__(self):
        self.tim = Turtle()
        self.create_road()
        self.create_mid()



    def create_road(self):
        self.tim.pencolor("yellow")
        self.tim.pensize(10)
        for y in range(-260, 300, 80):
            self.tim.penup()
            self.tim.goto(320,y)
            self.tim.pendown()
            self.tim.goto(-320,y)

    def create_mid(self):
        self.tim.pencolor("white")
        self.tim.pensize(5)
        for x in range(-240, 240, 40):
            self.tim.penup()
            self.tim.goto(-300, x)
            self.tim.pendown()
            for i in range(11):
                self.tim.forward(20)
                self.tim.penup()
                self.tim.forward(38)
                self.tim.pendown()

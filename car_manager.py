from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
ROAD = [0, 40, -40, 80, -80, 120, -120, 160, -160, 200, -200, -240]
LAST = 0


class CarManager():
    def __init__(self):
        self.cars = []
        self.carSpeed = STARTING_MOVE_DISTANCE

    def createCar(self):
        global LAST
        random_chance = random.randint(1, 6)
        if(random_chance == 1):
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            y = random.choice(ROAD)
            while(y == LAST):
                y = random.choice(ROAD)
            LAST = y
            if(y in [-200, -120, -40, 40, 120, 200]):
                car.goto(-300, y)
            else:
                car.goto(300, y)
                car.right(180)
            self.cars.append(car)


    def moveCar(self):
        for car in self.cars:
            car.forward(self.carSpeed)

    def levelUp(self):
        self.carSpeed += MOVE_INCREMENT

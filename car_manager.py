from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.cars = []
        self.carSpeed = STARTING_MOVE_DISTANCE

    def createCar(self):
        random_chance = random.randint(1, 6)
        if(random_chance == 1):
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)


    def moveCar(self):
        for car in self.cars:
            car.backward(self.carSpeed)

    def levelUp(self):
        self.carSpeed += MOVE_INCREMENT
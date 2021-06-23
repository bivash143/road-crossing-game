#! /usr/bin/python3
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.moveUp, "Up")
screen.onkey(player.moveDown, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.createCar()
    car.moveCar()
    
    for eachCar in car.cars:
        if( eachCar.distance(player) < 20):
            game_is_on = False
            scoreboard.game_over()

    if(player.ycor() > 280):
        player.go_to_start()
        car.levelUp()
        scoreboard.updateScore()

screen.exitonclick()

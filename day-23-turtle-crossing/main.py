import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize the turtles that we need
tim = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(tim.go_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # Detect colliison with cars
    for car in car_manager.all_cars:
        if car.distance(tim) < 20:
            game_is_on = False
            scoreboard.game_over()
            print("Ups! a car squish you :c")

    # Detect when tim survives
    if tim.has_finished():
        scoreboard.level_up()
        car_manager.increase_speed()
        print("Tim has reached the end of the road!")


screen.exitonclick()

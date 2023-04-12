import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
runner = Player()
level = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(key='Up', fun=runner.move_fwd)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    for car in cars.all_cars:
        if car.distance(runner) < 20:
            game_is_on = False
            level.game_over()
    if runner.ycor() >= 290:
        runner.reset_position()
        level.level_up()
        cars.speed_up()
        # level-up speed of the cars

screen.exitonclick()

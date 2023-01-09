import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# initialization of Game Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Player Initialization
player = Player()

# Control Player's movement across the screen
screen.listen()
screen.onkey(fun=player.move, key="Up")




# Initialize Scoreboard
score = Scoreboard()

# initialize car
car = CarManager()



game_is_on = True

# Body of the game 
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car.create_car()
    car.move()
    
    #  Detect players collision with top wall to level up 
    if player.ycor() >= 280:
        player.reset_player()
        score.increase_level()
        car.increase_speed()
        print(car.starting_move_distance)
    
    # Detect Collision with cars 
    for cars in car.all_cars:
        if player.distance(cars) == 25:
            score.game_over()
            game_is_on = not True

screen.exitonclick()
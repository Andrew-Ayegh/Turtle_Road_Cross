from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

MOVE_INCREMENT = 5

class CarManager(Turtle):
    def __init__(self):
        self.all_cars= []
        self.starting_move_distance = 5
        # self.increase_speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT
        
    def create_car(self):
        '''create new ar on the screen'''
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            # new_car.shape()
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250) )
            new_car.setheading(180)
            self.all_cars.append(new_car)
    
    def move(self):
        '''Move the car forward'''
        for car in self.all_cars:
            car.forward(self.starting_move_distance)
    
    def increase_speed(self):
        self.starting_move_distance += MOVE_INCREMENT
        
        

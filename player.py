from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.goto(STARTING_POSITION)
    
    def move(self):
        '''Move player forward'''
        self.forward(MOVE_DISTANCE)
    
    def reset_player(self):
        '''Take player back to the bottom of the screen'''
        self.goto(STARTING_POSITION)
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-200,250 )
        self.score()
    def score(self):    
        '''Display score of the player'''
        self.write(f"Level:{self.level} ", False, align='center', font=(FONT))
    
    def increase_level(self):
        '''Level up Game by 1 Level'''
        self.clear()
        self.level += 1
        self.write(f"Level:{self.level} ", False, align='center', font=(FONT))
    
    def game_over(self):
        '''End of game'''
        self.reset()
        self.write("Game Over ", False, align='center', font=(FONT))
    

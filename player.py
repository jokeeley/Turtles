from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    """creating the player class you can add in move_forward, reset_turtle, crossed_finish"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('black')
        self.right(-90)
        self.goto(0, -280)
        
    def move_forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        
    def reset_turtle(self):
        self.goto(STARTING_POSITION)
        
    def crossed_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
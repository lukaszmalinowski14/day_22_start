from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1, None)
        self.penup()
        self.goto(0, 0)
        self.kierunek_x = True
        self.kierunek_y = True

    def move(self, x=0):
        # detect padle x:
        # cal = 0
        # if x != 0 and self.xcor() > 0:
        #     cal = 20
        # elif x != 0 and self.xcor() < 0:
        #     cal = -20
        # GAME OVER
        # if self.xcor() > 340 or self.xcor() < -340:
        #     print("Game Over")
        #     self.goto(0, 0)

        if self.xcor()+x > 340:
            # print(self.xcor())
            self.kierunek_x = False
        # if self.ycor() > 280:
            # print(self.ycor())
            # self.kierunek_y = False
        # if self.ycor() < -280:
            # print(self.ycor())
            # self.kierunek_y = True
        if self.xcor()+x < -340:
            # print(self.xcor())
            self.kierunek_x = True
        if self.kierunek_x == True:
            new_x = self.xcor()+10
        else:
            new_x = self.xcor()-10
        if self.kierunek_y == True:
            new_y = self.ycor()+10
        else:
            new_y = self.ycor()-10

        self.goto(new_x, new_y)

    def bounce(self, direction):
        if direction == 'x':
            self.kierunek_x = not self.kierunek_x
        elif direction == 'y':
            self.kierunek_y = not self.kierunek_y

    def game_over(self):
        self.goto(0, 0)
        self.bounce('x')

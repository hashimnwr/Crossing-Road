from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(x=-290, y=270)
        self.update_score()

    def update_score(self):
        self.write(f'Level = {self.score}', align='left', font=FONT)

    def level_up(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER!', align='center', font=FONT)

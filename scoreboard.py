from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as DATA:
            self.high_score = int(DATA.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font=("Courier", 15, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as new_data:
                new_data.write(str(self.score))
            self.score = 0
            self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", align="center", font=("Courier", 15, "normal"))

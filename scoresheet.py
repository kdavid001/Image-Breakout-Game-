from turtle import Turtle

class Scores(Turtle):
    def __init__(self):
        super().__init__()
        with open("Highscore.txt") as score:
            self.highscore = int(score.read())
            self.highscore = int(self.highscore)
        self.clear()
        self.penup()
        self.setposition(0, 250)
        self.color('white')
        self.hideturtle()
        self.pad_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f"Score: {self.pad_score}", align='center', font=('Arial', 30, 'normal'))
        self.goto(100, 200)
        self.write(arg=f"Highscore: {self.highscore}", align='center', font=('Arial', 30, 'normal'))



    def paddle_point(self):
        self.pad_score += 1
        self.update()

    def reset_score(self):
        if self.pad_score > int(self.highscore):
            self.highscore = self.pad_score
            with open("Highscore.txt", 'w') as score:
                self.highscore = str(self.highscore)
                score.write(f"{self.highscore}")
        self.score = 0
        self.update()

    def highscore(self):
        return self.highscore






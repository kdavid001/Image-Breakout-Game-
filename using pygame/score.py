class Score:
    def __init__(self):
        self.score = 0
        self.highscore = self.load_highscore()

    def load_highscore(self):
        try:
            with open("Highscore.txt", "r") as file:
                return int(file.read())
        except:
            return 0

    def save_highscore(self):
        with open("Highscore.txt", "w") as file:
            file.write(str(self.highscore))

    def increase_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

    def check_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
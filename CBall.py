import random
class Ball:


    def __init__(self):
        self.x = random.randint(0,600)
        self.y = random.randint(0,600)
        self.radius = 10
        if self.x >= self.y:
            self.label = 1
        else:
            self.label = -1


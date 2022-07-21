import random

class Preceptron:
    weights = [0] * 2
    def __init__(self):
        for i in range(len(self.weights)):
            self.weights[i] = random.uniform(-1,1)
    def Guess(self, inputs):




